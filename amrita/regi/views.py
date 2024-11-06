from django.shortcuts import render,HttpResponse

# Create your views here.
def register(request):
    return HttpResponse("<html><body><h1>Welcome to Amrita's site</h1></body></html>")
