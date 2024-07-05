from django.contrib import admin
from. models import CustomUser, UserAndPetDetails, PetAndTrainerMapping

@admin.register(CustomUser)

class CustomUser_admin(admin.ModelAdmin):
    list_display =("id", "first_name", "last_name", "experience", "phone", "address", "picture", "email")

@admin.register(UserAndPetDetails)

class UseAndPetDetails_admin(admin.ModelAdmin):
    list_display=(
"id",
"first_name",
"last_name",
"email",
"phone",
"pet_name",
"pet_behavior",
"pet_age",
"meal_timing",
"discription",
"is_trainer_assigned",
"is_training_complete"
)
    
@admin.register(PetAndTrainerMapping)

class PetAndTrainerMapping_admin(admin.ModelAdmin):
    list_display =("id", "pet", "trainer")