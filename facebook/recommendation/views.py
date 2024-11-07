from django.shortcuts import render, HttpResponse
from recommendation.models import Person,Hobbies
def register(request):
    return HttpResponse("<html><body>This is a response</body></html>")

def registration(request):
    if request.method == "POST":
        name=request.POST['username']
        email = request.POST['email']
        print(name)
        ins=Person(username=name,email=email)
        ins.save()
        print("Success")
    context = {"website":"Amrita","course":"Full stack development"}
    return render(request,'register.html',context)

def hobbies(request):
    if request.method == "POST":
        username=request.POST['username']
        hobbies = request.POST['hobbies']
        ins=Hobbies(username=username,hobbies=hobbies)
        ins.save()
        print("Success")
    context = {"website":"Amrita","course":"Full stack development"}    
    return render(request,'hobbies.html',context)


