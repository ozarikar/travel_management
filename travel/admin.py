from django.contrib import admin
from .models import Sport, Trip, Traveler, TripTraveler, Booking, Expense

@admin.register(Sport)
class SportAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    list_display = ('name', 'destination', 'start_date', 'end_date')

@admin.register(Traveler)
class TravelerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'role', 'email']
    list_filter = ['role']
    search_fields = ['first_name', 'last_name', 'email']

@admin.register(TripTraveler)
class TripTravelerAdmin(admin.ModelAdmin):
    list_display = ['trip', 'traveler', 'per_diem_total']

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['trip', 'booking_type', 'vendor', 'start_datetime', 'cost_estimate']
    list_filter = ['booking_type', 'trip']

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ['trip', 'category', 'amount', 'description', 'incurred_at']
    list_filter = ['category', 'trip']