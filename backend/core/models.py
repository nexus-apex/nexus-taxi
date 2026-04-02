from django.db import models

class Ride(models.Model):
    ride_id = models.CharField(max_length=255)
    rider_name = models.CharField(max_length=255, blank=True, default="")
    rider_phone = models.CharField(max_length=255, blank=True, default="")
    pickup = models.CharField(max_length=255, blank=True, default="")
    dropoff = models.CharField(max_length=255, blank=True, default="")
    distance_km = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    fare = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    status = models.CharField(max_length=50, choices=[("requested", "Requested"), ("accepted", "Accepted"), ("in_progress", "In Progress"), ("completed", "Completed"), ("cancelled", "Cancelled")], default="requested")
    driver_name = models.CharField(max_length=255, blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.ride_id

class RideDriver(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255, blank=True, default="")
    email = models.EmailField(blank=True, default="")
    vehicle_make = models.CharField(max_length=255, blank=True, default="")
    vehicle_number = models.CharField(max_length=255, blank=True, default="")
    rating = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    trips_completed = models.IntegerField(default=0)
    status = models.CharField(max_length=50, choices=[("online", "Online"), ("on_trip", "On Trip"), ("offline", "Offline")], default="online")
    earnings_today = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name

class RideVehicle(models.Model):
    registration = models.CharField(max_length=255)
    make = models.CharField(max_length=255, blank=True, default="")
    model = models.CharField(max_length=255, blank=True, default="")
    vehicle_type = models.CharField(max_length=50, choices=[("mini", "Mini"), ("sedan", "Sedan"), ("suv", "SUV"), ("premium", "Premium"), ("auto", "Auto")], default="mini")
    year = models.IntegerField(default=0)
    driver_name = models.CharField(max_length=255, blank=True, default="")
    status = models.CharField(max_length=50, choices=[("active", "Active"), ("maintenance", "Maintenance"), ("retired", "Retired")], default="active")
    insurance_expiry = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.registration
