from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from .forms import UserRegistrationForm, LoginForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f"Account created for {username}")
            return redirect("login")
    else:
        form = UserRegistrationForm()
    context = {
        'form': form
    }
    return render(request, 'users/register.html', context)


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("password")

            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect("blog_home")
    else:
        form = LoginForm()
    context = {
        "form": form
    }
    return render(request, "users/login.html", context)


def logout_view(request):
    auth.logout(request)
    return render(request, "users/logout.html")

@login_required()
def user_profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,
                                instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile
                                   )
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f"Your profile has been updated!")
            return redirect("profile")

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, "users/profile.html", context)