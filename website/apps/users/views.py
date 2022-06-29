from django.shortcuts import render
from django.views.generic import View,  ListView, CreateView, UpdateView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy
from .models import Profile

# Create your views here.

def home(request):
	return render(request, 'users/home.html')

def dashboard(request):
	return render(request, 'users/dashboard.html')

class Signup(CreateView):
	form_class = UserCreationForm
	success_url = reverse_lazy('login')
	template_name = 'registration/signup.html'

class UserEditProfile(UpdateView):
	form_class = UserChangeForm
	success_url = reverse_lazy('userprofile')
	template_name = 'registration/user_editprofile.html'

	def get_object(self):
		return self.request.user

class Profile(ListView):
	model = Profile
	template_name = 'registration/user_profile.html'
