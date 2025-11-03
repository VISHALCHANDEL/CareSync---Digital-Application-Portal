from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='admin_login'),
    path('dashboard/', views.dashboard, name='admin_dashboard'),
]
