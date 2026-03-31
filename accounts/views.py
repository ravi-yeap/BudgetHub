from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.decorators.http import require_http_methods
from .forms import UserSignUpForm, UserLoginForm, UpdateProfileForm, ChangePasswordForm
from .models import StudentProfile


def signup_view(request):
    """User registration view."""
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Account created successfully! Please log in.')
            return redirect('login')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{field}: {error}')
    else:
        form = UserSignUpForm()
    
    return render(request, 'accounts/signup.html', {'form': form})


def login_view(request):
    """User login view."""
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            # Try to authenticate with username first, then email
            user = authenticate(request, username=username, password=password)
            if not user:
                try:
                    user_obj = User.objects.get(email=username)
                    user = authenticate(request, username=user_obj.username, password=password)
                except User.DoesNotExist:
                    pass
            
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {user.get_full_name() or user.username}!')
                return redirect('dashboard')
            else:
                messages.error(request, 'Invalid username/email or password.')
    else:
        form = UserLoginForm()
    
    return render(request, 'accounts/login.html', {'form': form})


@login_required(login_url='login')
def logout_view(request):
    """User logout view."""
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('login')


@login_required(login_url='login')
def profile_view(request):
    """User profile view."""
    student_profile = get_object_or_404(StudentProfile, user=request.user)
    return render(request, 'accounts/profile.html', {'student_profile': student_profile})


@login_required(login_url='login')
def update_profile_view(request):
    """Update user profile view."""
    student_profile = get_object_or_404(StudentProfile, user=request.user)
    
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, instance=student_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')
    else:
        form = UpdateProfileForm(instance=student_profile)
    
    return render(request, 'accounts/update_profile.html', {'form': form})


@login_required(login_url='login')
def change_password_view(request):
    """Change password view."""
    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            if request.user.check_password(form.cleaned_data['current_password']):
                request.user.set_password(form.cleaned_data['new_password'])
                request.user.save()
                login(request, request.user)
                messages.success(request, 'Password changed successfully!')
                return redirect('profile')
            else:
                messages.error(request, 'Current password is incorrect.')
    else:
        form = ChangePasswordForm()
    
    return render(request, 'accounts/change_password.html', {'form': form})


@login_required(login_url='login')
@require_http_methods(['POST'])
def delete_account_view(request):
    """Delete user account view."""
    user = request.user
    username = user.username
    user.delete()
    messages.success(request, f'Account {username} has been deleted.')
    return redirect('login')
