from django.urls import path
from . import views

urlpatterns = [
    path('add_trip', views.add_trip, name='add_trip'),
    path('trip/<int:trip_id>/apply', views.apply, name='apply'),
    path('trip/<int:trip_id>', views.current_trip, name='current_trip'),
    path('', views.trips, name='trips'),
]
