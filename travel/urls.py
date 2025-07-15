from django.urls import path
from . import views
from django.shortcuts import render

app_name = 'travel'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('dashboard/', views.dashboard, name='dashboard'),
]

def home(request):
    return render(request, 'travel/home.html')
