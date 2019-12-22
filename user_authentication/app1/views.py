from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.

def index(request):
    return render(request, 'app1/index.html')

def register(request):

    registered = False

    if request.method == "POST":
        user_form = forms.UserForm(data = request.POST)
        profile_form = forms.UserProfileInfoForm(data = request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit = False)
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit = False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']


            profile.save()

            registered = True

        else:
            print (user_form.errors, profile_form.errors)

    else:
        user_form = forms.UserForm()
        profile_form = forms.UserProfileInfoForm()

    return render(request, 'app1/registration.html', {'user_form':user_form, 'profile_form':profile_form, 'registered':registered})


def user_login(request):
    login_form = forms.LoginForm()

    if request.method == "POST":
        login_form = forms.LoginForm(data = request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']

            user = authenticate(username = username, password = password)

            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('index'))

                else:
                    return HttpResponse("User Not Active")

            else:
                print("wrong username and password combination")
                return HttpResponse("wrong username and password combination")



    return render(request, 'app1/login.html', {'login_form':login_form})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def special(request):
    return HttpResponse("You are logged in")