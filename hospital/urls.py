from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.hospital_register, name='hospital_register'),
    path('success/', views.hospital_success, name='hospital_success'),
]
