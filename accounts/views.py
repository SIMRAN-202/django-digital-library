from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileUpdateForm


def user_login(req):
    if req.user.is_authenticated:
        return redirect('home')  # Redirect if already logged in

    if req.method == 'POST':
        form = AuthenticationForm(data=req.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(req, user)
            messages.success(req, f"Welcome back, {user.username}!")
            return redirect('dashboard')
        else:
            messages.error(req, "Invalid username or password")
    else:
        form = AuthenticationForm()

    return render(req, 'login.html', {'form': form})


def register(req):
    if req.user.is_authenticated:
        return redirect('home')

    if req.method == 'POST':
        form = UserCreationForm(req.POST)
        if form.is_valid():
            user = form.save()
            auth_login(req, user)
            messages.success(req, "Account created successfully!")
            return redirect('home')
        else:
            messages.error(req, "Please correct the error below.")
    else:
        form = UserCreationForm()

    return render(req, 'register.html', {'form': form})


def user_logout(req):
    auth_logout(req)
    messages.info(req, "Logged out successfully.")
    return redirect('login')


@login_required
def dashboard(req):
    profile = req.user.profile
    return render(req, 'dashboard.html', {
        'profile': profile
    })


@login_required
def edit_profile(request):
    user = request.user
    profile = user.profile

    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)

        if form.is_valid():
            # Update user fields
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.email = form.cleaned_data['email']

            # Update password if provided
            new_password = form.cleaned_data.get('new_password')
            confirm_password = request.POST.get('confirm_password')

            if new_password:
                if new_password == confirm_password:
                    user.set_password(new_password)
                    update_session_auth_hash(request, user)  # important to avoid logout
                else:
                    messages.error(request, "Passwords do not match.")
                    return render(request, 'edit_profile.html', {'form': form})

            user.save()  # Save user model
            form.save()  # Save profile model
            messages.success(request, "Your profile has been updated successfully.")
            return redirect('dashboard')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        # Initial data for user fields
        initial_data = {
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
        }
        form = ProfileUpdateForm(instance=profile, initial=initial_data)

    return render(request, 'edit_profile.html', {'form': form})