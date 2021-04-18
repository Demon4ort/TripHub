from django.shortcuts import render
from .forms import UserForm


def register(request):
    form = UserForm()
    return render(request, 'registration_page.html', {'form': form})


def login(request):
    return render(request, 'login_page.html')
