from django.contrib.auth.decorators import login_required
from .models import Trip
from .forms import TripForm
from django.shortcuts import render, redirect

@login_required
def trip_list(request):
    trips = Trip.objects.all()
    return render(request, 'travel/trip_list.html', {'trips': trips})

@login_required
def add_trip(request):
    if request.method == 'POST':
        form = TripForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('travel:trip_list')
    else:
        form = TripForm()
    return render(request, 'travel/add_trip.html', {'form': form})

def home(request):
    """Homepage view"""
    context = {
        'title': 'Home',
        'hero_title': 'Travel Management System',
        'hero_subtitle': 'Streamline your athletic department travel planning',
    }
    return render(request, 'travel/home.html', context)

def about(request):
    """About page view"""
    context = {
        'title': 'About Us',
    }
    return render(request, 'travel/about.html', context)

def contact(request):
    """Contact page view"""
    context = {
        'title': 'Contact',
    }
    return render(request, 'travel/contact.html', context)

@login_required
def dashboard(request):
    """Dashboard view for authenticated users"""
    context = {
        'title': 'Dashboard',
        'user': request.user,
    }
    return render(request, 'travel/dashboard.html', context)