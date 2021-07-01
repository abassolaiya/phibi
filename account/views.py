from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import UserRegistrationForm, UserEditForm, ProfileEditForm
from .models import Profile, Contactus

# Create your views here.


def indexpage(request):
    return render(request,'account/homepage.html')

def aboutuspage(request):
    return render(request, 'pages/about.html')

def servicespage(request):
    return render(request, 'pages/services.html')

class ContactListView(LoginRequiredMixin, ListView):
    model = Contactus
    context_object_name = 'contact_list'
    template_name = 'general/contact_list.html'
    login_url = 'account_login'

class ContactCreateView(CreateView):
    model = Contactus
    template_name = 'pages/about.html'
    fields = ('name', 'email', 'phone_no', 'message')
    success_url = reverse_lazy('indexpage')

@login_required
def dashboard(request):
    return render(request,
        'account/dashboard.html',
        {'section': 'dashboard'})

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(
                user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            Profile.objects.create(user=new_user)
            return render(request,
                        'account/register_done.html',
                        {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,
        'account/register.html',
        {'user_form': user_form})

@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile,
                                    data=request.POST,
                                    files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated '\
            'successfully')
        else:
            messages.error(request, 'Error updating your profile')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request,
                'account/edit.html',
                {'user_form': user_form,
                'profile_form': profile_form})
