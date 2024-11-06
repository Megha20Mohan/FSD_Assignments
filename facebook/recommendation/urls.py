from django.contrib import admin
from django.urls import path,include
from recommendation import views

urlpatterns = [
    path('register/',views.registration, name='r'),
    path('hobbies/',views.hobbies, name='r')
]