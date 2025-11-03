from django.shortcuts import render

def home(request):
    return render(request, 'patient/home.html')

def login_view(request):
    return render(request, 'patient/login.html')

def signup_view(request):
    return render(request, 'patient/signup.html')
