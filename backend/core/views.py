import json
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Sum, Count
from .models import Ride, RideDriver, RideVehicle


def login_view(request):
    if request.user.is_authenticated:
        return redirect('/dashboard/')
    error = ''
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/dashboard/')
        error = 'Invalid credentials. Try admin / Admin@2024'
    return render(request, 'login.html', {'error': error})


def logout_view(request):
    logout(request)
    return redirect('/login/')


@login_required
def dashboard_view(request):
    ctx = {}
    ctx['ride_count'] = Ride.objects.count()
    ctx['ride_requested'] = Ride.objects.filter(status='requested').count()
    ctx['ride_accepted'] = Ride.objects.filter(status='accepted').count()
    ctx['ride_in_progress'] = Ride.objects.filter(status='in_progress').count()
    ctx['ride_total_distance_km'] = Ride.objects.aggregate(t=Sum('distance_km'))['t'] or 0
    ctx['ridedriver_count'] = RideDriver.objects.count()
    ctx['ridedriver_online'] = RideDriver.objects.filter(status='online').count()
    ctx['ridedriver_on_trip'] = RideDriver.objects.filter(status='on_trip').count()
    ctx['ridedriver_offline'] = RideDriver.objects.filter(status='offline').count()
    ctx['ridedriver_total_rating'] = RideDriver.objects.aggregate(t=Sum('rating'))['t'] or 0
    ctx['ridevehicle_count'] = RideVehicle.objects.count()
    ctx['ridevehicle_mini'] = RideVehicle.objects.filter(vehicle_type='mini').count()
    ctx['ridevehicle_sedan'] = RideVehicle.objects.filter(vehicle_type='sedan').count()
    ctx['ridevehicle_suv'] = RideVehicle.objects.filter(vehicle_type='suv').count()
    ctx['recent'] = Ride.objects.all()[:10]
    return render(request, 'dashboard.html', ctx)


@login_required
def ride_list(request):
    qs = Ride.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(ride_id__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(status=status_filter)
    return render(request, 'ride_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def ride_create(request):
    if request.method == 'POST':
        obj = Ride()
        obj.ride_id = request.POST.get('ride_id', '')
        obj.rider_name = request.POST.get('rider_name', '')
        obj.rider_phone = request.POST.get('rider_phone', '')
        obj.pickup = request.POST.get('pickup', '')
        obj.dropoff = request.POST.get('dropoff', '')
        obj.distance_km = request.POST.get('distance_km') or 0
        obj.fare = request.POST.get('fare') or 0
        obj.status = request.POST.get('status', '')
        obj.driver_name = request.POST.get('driver_name', '')
        obj.save()
        return redirect('/rides/')
    return render(request, 'ride_form.html', {'editing': False})


@login_required
def ride_edit(request, pk):
    obj = get_object_or_404(Ride, pk=pk)
    if request.method == 'POST':
        obj.ride_id = request.POST.get('ride_id', '')
        obj.rider_name = request.POST.get('rider_name', '')
        obj.rider_phone = request.POST.get('rider_phone', '')
        obj.pickup = request.POST.get('pickup', '')
        obj.dropoff = request.POST.get('dropoff', '')
        obj.distance_km = request.POST.get('distance_km') or 0
        obj.fare = request.POST.get('fare') or 0
        obj.status = request.POST.get('status', '')
        obj.driver_name = request.POST.get('driver_name', '')
        obj.save()
        return redirect('/rides/')
    return render(request, 'ride_form.html', {'record': obj, 'editing': True})


@login_required
def ride_delete(request, pk):
    obj = get_object_or_404(Ride, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/rides/')


@login_required
def ridedriver_list(request):
    qs = RideDriver.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(name__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(status=status_filter)
    return render(request, 'ridedriver_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def ridedriver_create(request):
    if request.method == 'POST':
        obj = RideDriver()
        obj.name = request.POST.get('name', '')
        obj.phone = request.POST.get('phone', '')
        obj.email = request.POST.get('email', '')
        obj.vehicle_make = request.POST.get('vehicle_make', '')
        obj.vehicle_number = request.POST.get('vehicle_number', '')
        obj.rating = request.POST.get('rating') or 0
        obj.trips_completed = request.POST.get('trips_completed') or 0
        obj.status = request.POST.get('status', '')
        obj.earnings_today = request.POST.get('earnings_today') or 0
        obj.save()
        return redirect('/ridedrivers/')
    return render(request, 'ridedriver_form.html', {'editing': False})


@login_required
def ridedriver_edit(request, pk):
    obj = get_object_or_404(RideDriver, pk=pk)
    if request.method == 'POST':
        obj.name = request.POST.get('name', '')
        obj.phone = request.POST.get('phone', '')
        obj.email = request.POST.get('email', '')
        obj.vehicle_make = request.POST.get('vehicle_make', '')
        obj.vehicle_number = request.POST.get('vehicle_number', '')
        obj.rating = request.POST.get('rating') or 0
        obj.trips_completed = request.POST.get('trips_completed') or 0
        obj.status = request.POST.get('status', '')
        obj.earnings_today = request.POST.get('earnings_today') or 0
        obj.save()
        return redirect('/ridedrivers/')
    return render(request, 'ridedriver_form.html', {'record': obj, 'editing': True})


@login_required
def ridedriver_delete(request, pk):
    obj = get_object_or_404(RideDriver, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/ridedrivers/')


@login_required
def ridevehicle_list(request):
    qs = RideVehicle.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(registration__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(vehicle_type=status_filter)
    return render(request, 'ridevehicle_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def ridevehicle_create(request):
    if request.method == 'POST':
        obj = RideVehicle()
        obj.registration = request.POST.get('registration', '')
        obj.make = request.POST.get('make', '')
        obj.model = request.POST.get('model', '')
        obj.vehicle_type = request.POST.get('vehicle_type', '')
        obj.year = request.POST.get('year') or 0
        obj.driver_name = request.POST.get('driver_name', '')
        obj.status = request.POST.get('status', '')
        obj.insurance_expiry = request.POST.get('insurance_expiry') or None
        obj.save()
        return redirect('/ridevehicles/')
    return render(request, 'ridevehicle_form.html', {'editing': False})


@login_required
def ridevehicle_edit(request, pk):
    obj = get_object_or_404(RideVehicle, pk=pk)
    if request.method == 'POST':
        obj.registration = request.POST.get('registration', '')
        obj.make = request.POST.get('make', '')
        obj.model = request.POST.get('model', '')
        obj.vehicle_type = request.POST.get('vehicle_type', '')
        obj.year = request.POST.get('year') or 0
        obj.driver_name = request.POST.get('driver_name', '')
        obj.status = request.POST.get('status', '')
        obj.insurance_expiry = request.POST.get('insurance_expiry') or None
        obj.save()
        return redirect('/ridevehicles/')
    return render(request, 'ridevehicle_form.html', {'record': obj, 'editing': True})


@login_required
def ridevehicle_delete(request, pk):
    obj = get_object_or_404(RideVehicle, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/ridevehicles/')


@login_required
def settings_view(request):
    return render(request, 'settings.html')


@login_required
def api_stats(request):
    data = {}
    data['ride_count'] = Ride.objects.count()
    data['ridedriver_count'] = RideDriver.objects.count()
    data['ridevehicle_count'] = RideVehicle.objects.count()
    return JsonResponse(data)
