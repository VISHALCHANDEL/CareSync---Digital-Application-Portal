from django.shortcuts import render

def home(request):
    return render(request, 'doctor/home.html')

def login_view(request):
    return render(request, 'doctor/login.html')

def signup_view(request):
    return render(request, 'doctor/signup.html')
