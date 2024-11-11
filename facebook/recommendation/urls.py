from django.contrib import admin
from django.urls import path,include
from recommendation import views

urlpatterns = [
    path("registration/",views.registration,name="r"),
    path("hobbies/",views.hobbies,name="r"),
    path("edit/",views.edit, name="r" )

]