from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect

from .forms import UserForm
from django.contrib.auth.models import User
from trips.models import Profile, Trip


@csrf_protect
def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            first_name = form.cleaned_data.get('first_name')
            second_name = form.cleaned_data.get('second_name')
            email = form.cleaned_data.get('email')
            facebook = form.cleaned_data.get('facebook')
            date_of_birth = form.cleaned_data.get('date_of_birth')
            phone = form.cleaned_data.get('phone')
            gender = form.cleaned_data.get('gender')
            user = User.objects.get(username=username)
            profile_new = Profile.objects.create(user=user, first_name=first_name,
                                                 second_name=second_name, facebook=facebook,
                                                 date_of_birth=date_of_birth, phone=phone,
                                                 gender=gender, email=email)
            profile_new.save()
            messages.success(request, f'Account created for {username}!')
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'registration_page.html', {'form': form})


@login_required
def log_out(request):
    logout(request)
    return redirect('index')


@login_required
def profile(request):
    parts = Trip.objects.filter(author_id=request.user.pk)
    context = {
        'trips': parts
    }
    return render(request, 'profile_page.html', context)
