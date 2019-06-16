from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegistrationForm
from django.contrib.auth import login, logout, authenticate
from .forms import SignupForm, UpdateUserForm, UpdateProfileForm
from django.contrib.auth.decorators import login_required
from blogs.models import Blog


def signup_view(request):
    if request.method == 'POST':
        signup_form = UserRegistrationForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            username = signup_form.cleaned_data.get('username')
            messages.success(request, f'Thank you for using our website. <br> <strong> You\'re amazing! <br> </strong> Now you can login as {username}!')
            return redirect('user:login')
    else:
        signup_form = UserRegistrationForm()
    context = {
        'form':signup_form
    }
    return render(request, 'users/signup.html', context)


def login_view(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(request, request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            user = authenticate(username=username, password=login_form.cleaned_data.get('password'))
            if user is not None:
                login(request, user)
                messages.success(request, f'Successfully logged in as <strong> {username} </strong> ')
                return redirect('blog:blogs')
    else:
        login_form = AuthenticationForm()
    context = {
        'form': login_form
    }
    return render(request, 'users/login.html', context)


def logout_view(request):
    logout(request)
    messages.success(request, 'You are logged out, <strong> login </strong> again')
    return redirect('user:login')


@login_required
def profile_view(request):
    queryset = Blog.objects.filter(author=request.user)
    print(queryset)
    return render(request, 'users/profile.html', {'queryset': queryset})


def profile_update(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        user_profile = UpdateProfileForm(
            request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and user_profile.is_valid():
            user_form.save()
            user_profile.save()
            messages.success(
                request, 'Your profile has been updated successfully')
            return redirect('user:profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        user_profile = UpdateProfileForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': user_profile
    }
    return render(request, 'users/update_profile.html', context)
