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
    path('add_nickname/', views.AddNickname.as_view(), name='add_nickname'),
    path('profile/<int:pk>/edit_nickname/', views.EditNickname.as_view(), name='edit_nickname'),
    path('user/<int:user_id>/add_picture/', views.add_picture, name='add_picture'),
    path('user/<int:user_id>/change_picture/', views.change_picture, name='change_picture'),
]