from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .forms import DoctorSignupForm, DoctorLoginForm
from .models import Doctor

# --- Signup ---
def doctor_signup(request):
    if request.method == 'POST':
        form = DoctorSignupForm(request.POST)
        if form.is_valid():
            doctor = form.save(commit=False)
            doctor.password = make_password(form.cleaned_data['password'])
            doctor.save()
            return redirect('doctor_login')
    else:
        form = DoctorSignupForm()
    return render(request, 'doctor/doctor_sign_up.html', {'form': form})


# --- Login ---
def doctor_login(request):
    if request.method == 'POST':
        form = DoctorLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            try:
                doctor = Doctor.objects.get(email=email)
            except Doctor.DoesNotExist:
                return render(request, 'doctor/doctor_login.html', {'form': form, 'error': "Invalid credentials"})

            if check_password(password, doctor.password):
                request.session['doctor_id'] = doctor.id
                return redirect('doctor_dashboard')
            else:
                return render(request, 'doctor/doctor_login.html', {'form': form, 'error': "Invalid credentials"})
    else:
        form = DoctorLoginForm()
    return render(request, 'doctor/doctor_login.html', {'form': form})


# --- Logout ---
def doctor_logout(request):
    if 'doctor_id' in request.session:
        del request.session['doctor_id']
    return redirect('doctor_login')


# --- Dashboard ---
def doctor_dashboard(request):
    doctor_id = request.session.get('doctor_id')
    if not doctor_id:
        return redirect('doctor_login')

    doctor = Doctor.objects.get(pk=doctor_id)

    # Demo values for now
    today_appointments = 5
    new_patients = 2
    total_patients = 20
    pending_reports = 3
    avg_rating = 4.5
    reviews = [
        {'patient': 'John Doe', 'rating': 5, 'comment': 'Great doctor!'},
        {'patient': 'Jane Smith', 'rating': 4, 'comment': 'Very helpful.'}
    ]

    return render(request, 'doctor/doctor_dashboard.html', {
        "doctor": doctor,
        "today_appointments": today_appointments,
        "new_patients": new_patients,
        "total_patients": total_patients,
        "pending_reports": pending_reports,
        "avg_rating": avg_rating,
        "reviews": reviews
    })
