from django.shortcuts import render
from django.http import HttpResponse
from .models import Trip

def home(request):
    return HttpResponse("Travel Management System - MVP")

def trip_list(request):
    trips = Trip.objects.all()
    return render(request, 'travel/trip_list.html', {'trips': trips})