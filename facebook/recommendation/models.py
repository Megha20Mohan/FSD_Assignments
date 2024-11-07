from django.db import models

# Create your models here.

class Person(models.Model):
    username = models.CharField(max_length=30)
    email = models.CharField(max_length=100, default='example@email.com')

class Hobbies(models.Model):
    username = models.CharField(max_length=30)
    hobbies = models.CharField(max_length=250)
