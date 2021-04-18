from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'registration_page.html', {'form': form})


def login(request):
    return render(request, 'login_page.html')
