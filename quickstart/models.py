from django.db import models


# Create your models here.

class Status(models.Model):
    position = models.CharField(max_length=100)
    departament = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.position} in {self.departament}"


class Employee(models.Model):
    full_name = models.CharField(max_length=100)
    birth_year = models.CharField(max_length=100)
    position = models.ForeignKey(Status, on_delete=models.CASCADE)
    salary = models.CharField(max_length=100)
