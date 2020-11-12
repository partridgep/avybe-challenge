from django.urls import path
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('account/signup', views.signup, name='signup'),
]