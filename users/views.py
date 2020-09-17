from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegistrationForm
from django.http import HttpResponseRedirect 
from django.contrib.auth.models import User 

def index(request):
   return render(request, 'pages/home.html')
   
def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'pages/register.html', {'form': form})

def show(request):  
    users = User.objects.all()  
    return render(request, 'pages/users.html', {'users': users})  

def edit(request, id):  
    user = User.objects.get(id=id)  
    form = RegistrationForm()
    return render(request,'pages/edit.html', {'user':user})  

def update(request, id):  
    users = User.objects.all() 
    user = User.objects.get(id=id)  
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.update()
            return render(request, 'pages/users.html', {'users': users}) 
    return render(request, 'pages/home.html')

def destroy(request, id):  
    users = User.objects.all() 
    user = User.objects.get(id=id)  
    user.delete()  
    return render(request, 'pages/users.html', {'users': users})  

def profile(request, id):  
    user = User.objects.get(id=id)  
    return render(request, 'pages/profile.html', {'user': user})  