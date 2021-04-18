from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
)


class UserForm(UserCreationForm):
    first_name = forms.CharField(label='First Name', max_length=100)
    second_name = forms.CharField(label='Last Name', max_length=100)
    email = forms.EmailField(label='Email')
    facebook = forms.URLField(label='Facebook')
    date_of_birth = forms.DateField(label='Date of birth')
    phone = forms.CharField(label='Phone number', max_length=10)
    gender = forms.ChoiceField(label='Choose your gender', choices=GENDER_CHOICES)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2',
                  'first_name', 'second_name', 'email',
                  'facebook', 'date_of_birth', 'phone', 'gender']


