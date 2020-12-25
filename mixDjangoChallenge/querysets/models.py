from django.db import models


# Create your models here.

# One to One Relationship

class Car(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Ceo(models.Model):
    car = models.OneToOneField(Car, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name


# One to Many Relationship

class CarModel(models.Model):
    name = models.CharField(max_length=255)
    cars = models.ForeignKey(Car, on_delete=models.SET_NULL, blank=True, null=True, related_name="models")

    def __str__(self):
        return self.name
