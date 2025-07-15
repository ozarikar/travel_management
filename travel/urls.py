from django.urls import path
from . import views
from django.shortcuts import render

app_name = 'travel'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('trips/', views.trip_list, name='trip_list'),
    path('trips/add/', views.add_trip, name='add_trip'),
]

def home(request):
    return render(request, 'travel/home.html')
def about(request):
    return render(request, 'travel/about.html')

def contact(request):
    return render(request, 'travel/contact.html')

def dashboard(request):
    return render(request, 'travel/dashboard.html')
