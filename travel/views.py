from django.shortcuts import render
from django.contrib.auth.decorators import login_required

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