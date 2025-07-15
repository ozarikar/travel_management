from django.db import models
from django.contrib.auth.models import User

STATUS_CHOICES = [
    ('planning', 'Planning'),
    ('booked', 'Booked'),
    ('completed', 'Completed'),
    ('cancelled', 'Cancelled'),
]

class Trip(models.Model):
    name = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} to {self.destination}"
class Sport(models.Model):
    name = models.CharField(max_length=80)
    
    def __str__(self):
        return self.name

    
    sport = models.ForeignKey('self', on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    destination_city = models.CharField(max_length=100)
    destination_state = models.CharField(max_length=50, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    purpose = models.TextField(blank=True)
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='planning')
    budget_estimate = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.title} - {self.destination_city}"

class Traveler(models.Model):
    ROLE_CHOICES = [
        ('athlete', 'Athlete'),
        ('coach', 'Coach'),
        ('staff', 'Staff'),
    ]
    
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class TripTraveler(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='travelers')
    traveler = models.ForeignKey(Traveler, on_delete=models.CASCADE)
    per_diem_total = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    
    class Meta:
        unique_together = ['trip', 'traveler']

class Booking(models.Model):
    BOOKING_TYPES = [
        ('flight', 'Flight'),
        ('hotel', 'Hotel'),
        ('bus', 'Bus/Van'),
        ('car', 'Rental Car'),
        ('other', 'Other'),
    ]
    
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='bookings')
    booking_type = models.CharField(max_length=20, choices=BOOKING_TYPES)
    vendor = models.CharField(max_length=100, blank=True)
    confirmation_number = models.CharField(max_length=50, blank=True)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    cost_estimate = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)
    cost_actual = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)
    notes = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.booking_type} - {self.vendor}"

class Expense(models.Model):
    CATEGORY_CHOICES = [
        ('meals', 'Meals'),
        ('transportation', 'Transportation'),
        ('lodging', 'Lodging'),
        ('equipment', 'Equipment'),
        ('other', 'Other'),
    ]
    
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='expenses')
    traveler = models.ForeignKey(Traveler, on_delete=models.CASCADE, null=True, blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    amount = models.DecimalField(max_digits=9, decimal_places=2)
    description = models.CharField(max_length=200)
    receipt = models.FileField(upload_to='receipts/', null=True, blank=True)
    incurred_at = models.DateTimeField()
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.category} - ${self.amount}"