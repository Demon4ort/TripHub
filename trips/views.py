from django.shortcuts import render

from .models import Trip


# Create your views here.


def trips(request):
    context = {
        'trips': Trip.objects.all().order_by('created_at')
    }
    return render(request, 'trips_page.html', context)
