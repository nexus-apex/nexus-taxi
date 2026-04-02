from django.urls import path
from . import views

urlpatterns = [
    path('', lambda r: views.redirect('/dashboard/')),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('rides/', views.ride_list, name='ride_list'),
    path('rides/create/', views.ride_create, name='ride_create'),
    path('rides/<int:pk>/edit/', views.ride_edit, name='ride_edit'),
    path('rides/<int:pk>/delete/', views.ride_delete, name='ride_delete'),
    path('ridedrivers/', views.ridedriver_list, name='ridedriver_list'),
    path('ridedrivers/create/', views.ridedriver_create, name='ridedriver_create'),
    path('ridedrivers/<int:pk>/edit/', views.ridedriver_edit, name='ridedriver_edit'),
    path('ridedrivers/<int:pk>/delete/', views.ridedriver_delete, name='ridedriver_delete'),
    path('ridevehicles/', views.ridevehicle_list, name='ridevehicle_list'),
    path('ridevehicles/create/', views.ridevehicle_create, name='ridevehicle_create'),
    path('ridevehicles/<int:pk>/edit/', views.ridevehicle_edit, name='ridevehicle_edit'),
    path('ridevehicles/<int:pk>/delete/', views.ridevehicle_delete, name='ridevehicle_delete'),
    path('settings/', views.settings_view, name='settings'),
    path('api/stats/', views.api_stats, name='api_stats'),
]
