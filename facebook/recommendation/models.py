from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=30)

    #email=models.EmailField()

class Student(models.Model):
    hobbies = models.CharField(max_length=20)
    #roll_no = models.CharField(max_length=20)