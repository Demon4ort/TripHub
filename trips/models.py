from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Trip(models.Model):
    name_tr = models.CharField(max_length=40, unique=True)
    destination = models.CharField(max_length=30)
    description = models.TextField()
    requirements = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, related_name='trips', on_delete=models.CASCADE)
    DIFFICULTY_LEVELS = (
        ('VE', 'Very Easy'),
        ('ES', 'Easy'),
        ('ME', 'Medium'),
        ('HR', 'Hard'),
        ('VH', 'Very Hard'),
    )
    difficulty_level = models.CharField(max_length=30, choices=DIFFICULTY_LEVELS)

    def __str__(self):
        return self.name_tr


class Participation(models.Model):
    trip = models.ForeignKey(Trip, related_name='participation', on_delete=models.CASCADE)
    applied_by = models.ForeignKey(User, related_name='participation', on_delete=models.CASCADE)
    applied_at = models.DateTimeField(auto_now_add=True)


GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    email = models.EmailField()
    facebook = models.URLField()
    date_of_birth = models.DateField()
    phone = models.CharField(max_length=10)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
