from django.shortcuts import render, redirect
from .forms import HospitalForm

def hospital_register(request):
    if request.method == 'POST':
        form = HospitalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hospital_success')  # or any success page you have
    else:
        form = HospitalForm()
    return render(request, 'hospital/hospital_register.html', {'form': form})

def hospital_success(request):
    return render(request, 'hospital/hospital_success.html')