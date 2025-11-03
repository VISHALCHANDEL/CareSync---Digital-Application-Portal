from django import forms
from .models import Hospital, Department

class HospitalForm(forms.ModelForm):
    emergency_services = forms.ChoiceField(
        choices=[(True, 'Yes'), (False, 'No')],
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    departments = forms.ModelChoiceField(
        queryset=Department.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label="Select Department"
    )

    class Meta:
        model = Hospital
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'registration_number': forms.TextInput(attrs={'class': 'form-control'}),
            'hospital_type': forms.Select(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'pincode': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_number': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'website': forms.URLInput(attrs={'class': 'form-control'}),
            'established_year': forms.NumberInput(attrs={'class': 'form-control'}),
            'total_beds': forms.NumberInput(attrs={'class': 'form-control'}),
        }
