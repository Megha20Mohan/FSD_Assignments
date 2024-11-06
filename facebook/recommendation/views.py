from django.shortcuts import render, HttpResponse

def recommend(request):
    return HttpResponse("This is friends recommendation page")

def hobbies(request):
    if request.method=='POST':
        hobbies=request.POST['hobbies']
        print(hobbies)
        ins=Student(hobbies=hobbies)
        ins.save()
        print("Success")

    context={'website':'Amrita', 'course':'FSD'}
    return render(request,'hobbies.html',context)

def registration(request):
    if request.method=='POST':
        name=request.POST['firstname']
        print(name)
        ins=Person(first_name=name)
        ins.save()
        print("Success")

    context={'website':'Amrita', 'course':'FSD'}
    return render(request,'register.html',context)