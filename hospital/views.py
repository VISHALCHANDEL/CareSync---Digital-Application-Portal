from django.shortcuts import render, redirect
from .forms import HospitalForm
from .models import Hospital, HospitalImage
from django.contrib.auth.hashers import check_password
from django.contrib import messages

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


def hospital_login(request):
    if request.method == "POST":
        reg_no = request.POST.get("registration_number")
        password = request.POST.get("password")

        try:
            hospital = Hospital.objects.get(registration_number=reg_no)
            if check_password(password, hospital.password):
                # Login successful
                request.session['hospital_id'] = hospital.id  # store in session
                messages.success(request, f"Welcome {hospital.name}!")
                return redirect('hospital_dashboard')  # replace with your dashboard
            else:
                messages.error(request, "Invalid password.")
        except Hospital.DoesNotExist:
            messages.error(request, "Hospital with this registration number does not exist.")

    return render(request, "hospital/hospital_login.html")

#  Dashboard View for the hospital
def hospital_dashboard(request):
    hospital_id = request.session.get("hospital_id")

    if not hospital_id:
        return redirect("hospital_login")

    hospital = Hospital.objects.get(id=hospital_id)

    # Upload image
    if request.method == "POST" and request.FILES.get("image"):
        HospitalImage.objects.create(
            hospital=hospital,
            image=request.FILES["image"]
        )
        return redirect("hospital_dashboard")

    images = hospital.images.all()

    return render(request, "hospital/hospital_dashboard.html", {
        "hospital": hospital,
        "images": images
    })