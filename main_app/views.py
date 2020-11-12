from django.shortcuts import render, redirect
from .models import Profile, Picture
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# VIEWS

@login_required
def home(request):
    user = request.user
    return render(request, 'home.html', {
        'user': user
        })

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

# Class-based views

class AddNickname(LoginRequiredMixin, CreateView):
    model = Profile
    fields = ['nickname'] 

    def form_valid(self, form):
        # Assign the logged in user (self.request.user)
        form.instance.user = self.request.user  
        # Let the CreateView do its job as usual
        return super().form_valid(form)

class EditNickname(LoginRequiredMixin, UpdateView):
    model = Profile
    fields = ['nickname'] 