from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from shared_app.models  import Breed, TrainingType


class CustomUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, experience, phone, password=None,**extra_fields):
        '''
        Creates and save a User with the given email, first name, last name, and password. 
        '''
        if not email:
            raise ValueError('The Email field must be set')

        # Using normalize_email for lower case.

        print(f"{email=}")
        print(f"{first_name=}")
        print(f"{last_name=}")
        print(f"{experience=}")
        print(f"{phone=}")
        print(f"{password=}")
        
        email = self.normalize_email(email)
        user = self.model(
            email = email,
            first_name = first_name,
            last_name = last_name,
            experience = experience,
            phone = phone,
            **extra_fields
            )       
        # For  incryting password.
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, first_name, last_name, experience, phone, password=None,**extra_fields):
        '''
        Creates and saves a superuser with the given email, first name, last name, and password.
        '''
          # if is_staff is fasle then user unable to login.
        # if  is_superuser is false user have no permission to perform curd operation.
        print(f"{email=}")
        print(f"{first_name=}")
        print(f"{last_name=}")
        print(f"{experience=}")
        print(f"{phone=}")
        print(f"{password=}")
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        

        return self.create_user(email, first_name, last_name, experience, phone, password,**extra_fields)  
       

class CustomUser(AbstractUser):
    # Removing the user name field
    username = None

    # Making email field mandatory and unique
    email = models.EmailField(unique=True)

    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    experience = models.PositiveSmallIntegerField()
    phone = models.PositiveBigIntegerField()
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    # Defining optional fields 
    address = models.TextField()
    picture = models.ImageField()

    # Defining the email for user login Field
    USERNAME_FIELD = 'email'

    # Defining the mandatory fields
    REQUIRED_FIELDS = ['first_name', 'last_name', 'experience', 'phone']

    objects = CustomUserManager()

    def __str__(self):
        return self.first_name + " " + self.last_name


class UserAndPetDetails(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    email = models.EmailField()
    phone = models.PositiveBigIntegerField()
    pet_name = models.CharField(max_length= 50)
    pet_behavior = models.CharField(max_length=200)
    pet_age = models.CharField(max_length = 100)
    meal_timing = models.CharField(max_length= 200)
    breed_of_dog = models.OneToOneField(Breed, on_delete=models.CASCADE)
    type_of_training = models.OneToOneField(TrainingType, on_delete=models.CASCADE)
    discription = models.TextField()
    is_trainer_assigned = models.BooleanField(default= False)
    is_training_complete = models.BooleanField(default= False)

    def __str__(self):
        return self.pet_name

class PetAndTrainerMapping(models.Model):
    pet = models.ForeignKey(UserAndPetDetails, on_delete=models.CASCADE)
    trainer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pet)