from django import forms
from .models import Hospital

class HospitalForm(forms.ModelForm):
    # Make password hidden
    password = forms.CharField(
        widget=forms.PasswordInput(),
        label="Password"
    )

    class Meta:
        model = Hospital
        fields = [
            'name',
            'registration_number',
            'hospital_type',
            'address',
            'city',
            'state',
            'pincode',
            'contact_number',
            'email',
            'website',
            'established_year',
            'total_beds',
            'emergency_services',
            'password'
        ]
