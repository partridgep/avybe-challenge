from django.shortcuts import render, redirect
from .models import Profile, Picture
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# VIEWS

@login_required
def home(request):
    return render(request, 'home.html')

def signup(request):
    error_message = ''
    if request.method == 'POST':
        print(request.POST)
         # Create a user form object
         # that includes data from the browser
        form = SignUpForm(request.POST)
        if form.is_valid():
            # add user to database
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid sign up, try again!'
    # either a bad POST request, or a GET request
    # just render the empty form
    form = SignUpForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)