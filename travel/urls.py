# Create the travel app urls.py file
travel_urls_content = '''from django.urls import path
from . import views

app_name = 'travel'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
'''

with open('travel_urls.py', 'w') as f:
    f.write(travel_urls_content)

print("✅ travel/urls.py created")