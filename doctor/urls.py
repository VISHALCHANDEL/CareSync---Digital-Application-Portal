from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='doctor_home'),
    path('login/', views.login_view, name='doctor_login'),
    path('signup/', views.signup_view, name='doctor_signup'),
]
