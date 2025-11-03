from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='patient_home'),
    path('login/', views.login_view, name='patient_login'),
    path('signup/', views.signup_view, name='patient_signup'),
]
