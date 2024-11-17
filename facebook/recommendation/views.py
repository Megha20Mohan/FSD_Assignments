from django.shortcuts import render, HttpResponse
from recommendation.models import Person,Hobbies
from .forms import RecommendationForm
def registration(request):
    reg=RecommendationForm()
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

# def data1(request):
#     dataset = Person.objects.all
#     context = {"db":data1,}
#     return(request,'response.html',context)

def edit(request,pk):
    row_to_edit=Person.objects.get(pk=pk)
    if request.POST:
        username=request.POST.get('username')
        row_to_edit.username=username
        row_to_edit.save()
        dataset=Person.objects.all()
        return render(request, 'response1.html', {'db':dataset})


    reg=RecommendationForm(instance=row_to_edit)
    return render(request,'edit.html',{'reg1':reg})

def response_list(request):
    dataset = Person.objects.all()
    return render(request, 'response1.html', {'db': dataset})


def delete(request,pk):
    row=Person.objects.get(pk=pk)
    row.delete()
    dataset=Person.objects.all()
    return render(request,'response1.html',{'db':dataset})