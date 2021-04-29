from django import forms
from .models import DIFFICULTY_LEVELS, Trip


class TripForm(forms.Form):
    tripName = forms.CharField(max_length=100, label='Trip Name')
    destination = forms.CharField(max_length=100, label='Destination')
    google_link = forms.URLField(label='Google link')
    startDate = forms.DateField(label='Date of trip')
    numberOfParticipants = forms.IntegerField(min_value=5, max_value=40, label='Number of participants')
    description = forms.CharField(widget=forms.Textarea, max_length=1000, label='Description')
    requirements = forms.CharField(widget=forms.Textarea, max_length=1000, label='requirements')
    difficulty = forms.ChoiceField(choices=DIFFICULTY_LEVELS, label='Difficulty')

    class Meta:
        model = Trip
        fields = [
            'tripName', 'destination', 'google_link', 'startDate',
            'numberOfParticipants', 'description', 'requirements', 'difficulty',
        ]
