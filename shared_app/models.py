from django.db import models


class Breed(models.Model):
    breed_of_dog = models.CharField(max_length = 200)
    discription = models.TextField()

class TrainingType(models.Model):
    type_of_training = models.CharField(max_length = 200)
    discription = models.TextField()
    duration = models.PositiveSmallIntegerField()
    cost = models.PositiveBigIntegerField()