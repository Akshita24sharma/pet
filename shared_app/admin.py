from django.contrib import admin
from .models import Breed, TrainingType

@admin.register(Breed)

class Breed_admin(admin.ModelAdmin):
    list_display = ("id","breed_of_dog","discription")


@admin.register(TrainingType)

class TrainingType_admin(admin.ModelAdmin):
    list_display = ("id","type_of_training","discription","duration","cost")