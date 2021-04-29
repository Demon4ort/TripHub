from django.contrib import admin
from .models import Trip, Participation, Profile

# Register your models here.
admin.site.register(Trip)
admin.site.register(Participation)
admin.site.register(Profile)
