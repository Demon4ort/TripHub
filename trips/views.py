from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

from .forms import TripForm
from .models import Trip, Participation


# Create your views here.

@login_required
def trips(request):
    tripses = Trip.objects.all().order_by('created_at')
    res_trips = []
    for trip in tripses:
        parts_num = Participation.objects.filter(trip_id=trip.pk).count()
        if trip.numberOfParticipants > parts_num:
            res_trips += [trip]
    context = {
        'trips': res_trips
    }
    return render(request, 'trips_page.html', context)


@login_required
def add_trip(request):
    if request.method == 'POST':
        form = TripForm(request.POST)
        if form.is_valid():
            user = request.user
            tripName = form.cleaned_data.get('tripName')
            destination = form.cleaned_data.get('destination')
            google_link = form.cleaned_data.get('google_link')
            startDate = form.cleaned_data.get('startDate')
            numberOfParticipants = form.cleaned_data.get('numberOfParticipants')
            description = form.cleaned_data.get('description')
            requirements = form.cleaned_data.get('requirements')
            difficulty = form.cleaned_data.get('difficulty')
            trip = Trip.objects.create(name_tr=tripName, destination=destination, google_link=google_link,
                                       startDate=startDate, numberOfParticipants=numberOfParticipants,
                                       description=description,
                                       requirements=requirements, difficulty_level=difficulty, author=user)
            trip.save()
            messages.success(request, f'Trip created for {user.username}!')
            return redirect('trips')
    else:
        form = TripForm()
    return render(request, 'trip_adder.html', {'form': form})


@login_required
def current_trip(request, trip_id):
    trip = get_object_or_404(Trip, pk=trip_id)
    parts = Participation.objects.filter(trip=trip)
    num = parts.count()
    context = {
        'trip': trip,
        'parts': parts,
        'number': num,
    }
    return render(request, 'current_trip.html', context)


@login_required
def apply(request, trip_id):
    trip = get_object_or_404(Trip, pk=trip_id)
    part = Participation.objects.create(trip=trip, applied_by=request.user)
    part.save()
    messages.success(request, f'You applied for {trip.name_tr}!')
    return redirect('index')
