from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')
    
def signin(request):
    return render(request, 'signin.html')
    