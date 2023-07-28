from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login
# Create your views here.

def home(request):
    return render(request, 'home.html')
    
def signin(request):
    return render(request, 'signin.html')
    
# Created user | sign up new user
    
def signup(request):
    
    if request.method == 'GET':
        return render(request, 'signup.html')
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('veterinaria')
            except IntegrityError:
                return render(request, 'signup.html',{
                    'error' : 'user already exist'
                })
        return render(request, 'signup.html',{
            'error' : 'password do not match'
        })
        
def veterinaria(request):
    return render(request, 'veterinaria.html')