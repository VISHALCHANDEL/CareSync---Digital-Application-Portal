from django.shortcuts import render

def login_view(request):
    return render(request, 'care_admin/login.html')

def dashboard(request):
    return render(request, 'care_admin/dashboard.html')
