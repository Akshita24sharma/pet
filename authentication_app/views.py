from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.contrib.auth import get_user_model, authenticate, login
from shared_app.models  import Breed, TrainingType
from .models import Breed, TrainingType, UserAndPetDetails, PetAndTrainerMapping
from django.contrib import messages


CustomUser = get_user_model()

class HomeView(View):
    def get(self, request):
        print("Inside the home view get.")
        return render(request,"home.html")
        

class RegisterView(View):
    def get(self, request):
        print("Inside the get of register.")
        return render(request,'register.html')
    
    def post(self, request):
        print("Inside the post of register")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        experience = request.POST.get("experience")
        address = request.POST.get("address")
        password = request.POST.get("password")

        print(f'{first_name=}')
        print(f'{last_name=}')
        print(f'{phone=}')
        print(f'{address=}')
        print(f'{experience=}')
        print(f'{email=}')
        print(f'{password=}')

        obj = CustomUser.objects.create_user(
        first_name = first_name,
        last_name = last_name,
        phone = phone,
        address = address,
        experience = experience,
        email = email,
        password = password
        )
        return redirect("authentication_app:login")
    

class LoginView(View):
    def get(self,request):
        print("Inside the login view get.")
        return render(request,"login.html")
    
    def post(self,request):
        print("Indide the login view post.")
        email = request.POST.get("email")
        password = request.POST.get("password")

        print(f"{email=}")
        print(f"{password=}")

        # Authenticate checks user exist or not, if user exist it returns the user instance.
        # if no user is found it return None.
        user = authenticate(request, email= email, password= password)

        if user is not None:
            # we are using login to create the session also it binds the user instance with request.
            login(request,user)
            return redirect("authentication_app:dashboard")
        else:
            return ("Invaild details")
        

class DashboardView(View):
    def get(self, requset):
        print("Inside the home view get.")
        return render(requset,"dashboard.html")
    
class ListView(View):
    def get(self, request):
        print("Inside the list view get")

        assigned_obj = PetAndTrainerMapping.objects.filter(trainer=request.user)
        print("assigned_obj : ", assigned_obj)

        unassigned_obj= UserAndPetDetails.objects.filter(is_trainer_assigned= False, is_training_complete= False)
        print("unassign_obj : ", unassigned_obj)

        print('----'*20)

        pet_data = []

        for i in assigned_obj:
            if i.pet.is_training_complete == False:
                pet_data.append(i.pet)

        for i in unassigned_obj:
            pet_data.append(i)
        
        print(pet_data)

        # obj= UserAndPetDetails.objects.filter(is_trainer_assigned= False)
        obj= UserAndPetDetails.objects.all()
        print(f"++++++++++++{request.user}")
        print(f"++++++++++++{request.user.is_anonymous}")
        # we are using anonymous so that no one can view are data without logging in.
        if not request.user.is_anonymous:
            return render(request, "list.html",{"obj":pet_data})
        else:
            return HttpResponse("You are not allowed to view this content.")


class UserAndPetDetailsView(View):
    def get(self, request):
        print("Inside the pet details view get.")
        breed_obj = Breed.objects.all()
        training_type_obj = TrainingType.objects.all()
        return  render(request,"pet_details.html", {"breed_obj":breed_obj, "training_type_obj":training_type_obj})
    
    def post(slef, request):
        print("Inside the pet details view post.")
        print("Request post:-", request.POST)
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        pet_name= request.POST.get("pet_name")
        pet_behavior= request.POST.get("pet_behavior")
        pet_age= request.POST.get("pet_age")
        meal_timing= request.POST.get("meal_timing")
        breed_of_dog= request.POST.get("breed_of_dog")
        type_of_training= request.POST.get("type_of_training")
        discription= request.POST.get("discription")

        print(f"{first_name=}")
        print(f"{last_name=}")
        print(f"{email=}")
        print(f"{phone=}")
        print(f"{pet_name=}")
        print(f"{pet_behavior=}")
        print(f"{pet_age=}")
        print(f"{meal_timing=}")
        print(f"{breed_of_dog=}")
        print(f"{type_of_training=}")
        print(f"{discription=}")

        breed_obj= Breed.objects.get(id = breed_of_dog)
        training_type_obj= TrainingType.objects.get(id = type_of_training)
        
        # In this method we simpliy gave the id  to breed_of_dog_id and type_of_training_id.
        # user_and_pet= UserAndPetDetails.objects.create(
        # first_name=first_name,
        # last_name=last_name,
        # email=email,
        # phone=phone,
        # pet_name=pet_name,
        # pet_behavior=pet_behavior,
        # pet_age=pet_age,
        # meal_timing=meal_timing,
        # breed_of_dog_id=breed_of_dog,
        # type_of_training_id=type_of_training,
        # discription=discription
        # )
        #Left variables are table column and right side html data

        user_and_pet= UserAndPetDetails.objects.create(
        first_name=first_name,
        last_name=last_name,
        email=email,
        phone=phone,
        pet_name=pet_name,
        pet_behavior=pet_behavior,
        pet_age=pet_age,
        meal_timing=meal_timing,
        breed_of_dog=breed_obj,
        type_of_training=training_type_obj,
        discription=discription
        )

        messages.add_message(request, messages.INFO, "Your request is submitted. Please wait for our trainer revert. Thank you!")
        return redirect("authentication_app:home")
    
class StartTrainingView(View):
    def post(self, request):
        print("Inside the  start training post view.")
        pet_id = request.POST.get("pet_id")
        print(f"{pet_id=}")
        
        pet_obj= UserAndPetDetails.objects.get(id = pet_id) 
        print(f"{pet_obj=}")
        print(f"{pet_obj.is_trainer_assigned=}")

        pet_obj.is_trainer_assigned = True

        pet_obj.save()

        trainer_obj = request.user
        # While saving the data always take the left variable name same as in model Field otherwise it will  lead you to a type error.
        pet_trainer_obj = PetAndTrainerMapping.objects.create(pet = pet_obj, trainer = trainer_obj)

        current_user = request.user.id 
        print(f"---------------{current_user=}")

        print(f"-------------------{pet_trainer_obj=}")
        
        print(f"{pet_obj.is_trainer_assigned=}")

        return redirect("authentication_app:list")
    
class CompleteTrainingView(View):
    def get (self, request):
        print("Inside the complete training post view")

        assigned_obj = PetAndTrainerMapping.objects.filter(trainer=request.user)
        print("assigned_obj : ", assigned_obj)

        pet_data = []

        for i in assigned_obj:
            if i.pet.is_training_complete == True:
                pet_data.append(i.pet)

        return  render(request,"completed_training.html", {"obj":pet_data})

        
    def post(self, request):
        print("Inside the complete training post view")
        pet_id = request.POST.get("pet_id")
        print(f"{pet_id=}")
        
        pet_obj= UserAndPetDetails.objects.get(id = pet_id) 
        print(f"{pet_obj=}")
        pet_obj.is_training_complete = True
        pet_obj.save()

        return redirect("authentication_app:list")


        