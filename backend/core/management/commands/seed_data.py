from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from core.models import Ride, RideDriver, RideVehicle
from datetime import date, timedelta
import random


class Command(BaseCommand):
    help = 'Seed NexusTaxi with demo data'

    def handle(self, *args, **kwargs):
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@nexustaxi.com', 'Admin@2024')
            self.stdout.write(self.style.SUCCESS('Admin user created'))

        if Ride.objects.count() == 0:
            for i in range(10):
                Ride.objects.create(
                    ride_id=f"Sample {i+1}",
                    rider_name=f"Sample Ride {i+1}",
                    rider_phone=f"+91-98765{43210+i}",
                    pickup=f"Sample {i+1}",
                    dropoff=f"Sample {i+1}",
                    distance_km=round(random.uniform(1000, 50000), 2),
                    fare=round(random.uniform(1000, 50000), 2),
                    status=random.choice(["requested", "accepted", "in_progress", "completed", "cancelled"]),
                    driver_name=f"Sample Ride {i+1}",
                )
            self.stdout.write(self.style.SUCCESS('10 Ride records created'))

        if RideDriver.objects.count() == 0:
            for i in range(10):
                RideDriver.objects.create(
                    name=["Rajesh Kumar","Priya Sharma","Amit Patel","Deepa Nair","Vikram Singh","Ananya Reddy","Suresh Iyer","Meera Joshi","Karthik Rao","Fatima Khan"][i],
                    phone=f"+91-98765{43210+i}",
                    email=f"demo{i+1}@example.com",
                    vehicle_make=f"Sample {i+1}",
                    vehicle_number=f"Sample {i+1}",
                    rating=round(random.uniform(1000, 50000), 2),
                    trips_completed=random.randint(1, 100),
                    status=random.choice(["online", "on_trip", "offline"]),
                    earnings_today=round(random.uniform(1000, 50000), 2),
                )
            self.stdout.write(self.style.SUCCESS('10 RideDriver records created'))

        if RideVehicle.objects.count() == 0:
            for i in range(10):
                RideVehicle.objects.create(
                    registration=f"Sample {i+1}",
                    make=f"Sample {i+1}",
                    model=f"Sample {i+1}",
                    vehicle_type=random.choice(["mini", "sedan", "suv", "premium", "auto"]),
                    year=random.randint(1, 100),
                    driver_name=f"Sample RideVehicle {i+1}",
                    status=random.choice(["active", "maintenance", "retired"]),
                    insurance_expiry=date.today() - timedelta(days=random.randint(0, 90)),
                )
            self.stdout.write(self.style.SUCCESS('10 RideVehicle records created'))
