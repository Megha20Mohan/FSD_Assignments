from django.contrib import admin
from django.urls import path,include
from recommendation import views


urlpatterns = [
    path('registration/', views.registration, name='register'),
    path('hobbies/', views.hobbies, name='hobbies'),
    #path("list/", views.list, name='data1'),
    path('response/', views.response_list, name='list'),  # Updated list view
    path('edit/<int:pk>/', views.edit, name='edit'),
    path('delete/<int:pk>/', views.delete, name='delete'),
]