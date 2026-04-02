from django.contrib import admin
from .models import Ride, RideDriver, RideVehicle

@admin.register(Ride)
class RideAdmin(admin.ModelAdmin):
    list_display = ["ride_id", "rider_name", "rider_phone", "pickup", "dropoff", "created_at"]
    list_filter = ["status"]
    search_fields = ["ride_id", "rider_name", "rider_phone"]

@admin.register(RideDriver)
class RideDriverAdmin(admin.ModelAdmin):
    list_display = ["name", "phone", "email", "vehicle_make", "vehicle_number", "created_at"]
    list_filter = ["status"]
    search_fields = ["name", "phone", "email"]

@admin.register(RideVehicle)
class RideVehicleAdmin(admin.ModelAdmin):
    list_display = ["registration", "make", "model", "vehicle_type", "year", "created_at"]
    list_filter = ["vehicle_type", "status"]
    search_fields = ["registration", "make", "model"]
