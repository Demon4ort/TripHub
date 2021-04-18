"""TripHub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views as home_view
from users import views as users_view
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('trips/', include('trips.urls')),
    path('guides/', home_view.guide, name='guides'),
    path('guides/1', home_view.guide_1, name='guide1'),
    path('guides/2', home_view.guide_2, name='guide2'),
    path('register/', users_view.register, name='register'),
    path('login/', auth_view.LoginView.as_view(template_name='login_page.html'), name='login'),
    path('', home_view.index, name='index'),
]
