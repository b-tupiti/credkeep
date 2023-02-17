from django.contrib.auth import login, authenticate, logout, get_user_model
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm, CustomUserCreationForm


# Create your views here.
def loginUser(request):
    
    page = 'login'
    context = { 'page':page}

    if request.user.is_authenticated:
        return redirect('accounts')

    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(request.GET['next'] if 'next' in request.GET else 'accounts')

        else:
            messages.error(request, 'Username OR password is incorrect')

    return render(request, 'users/login_signup.html', context)

def logoutUser(request):
    if request.user.is_authenticated:
        logout(request)
        messages.info(request, 'User was logged out!')
    return redirect('login')

@login_required(login_url="login")
def editUserAccount(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been updated')
            return redirect('profile')

    context = {'form': form}
    return render(request, 'users/edit_profile.html', context)

def signUp(request):

    if request.user.is_authenticated:
        return redirect('accounts')

    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'User account was created!')

            login(request, user)
            return redirect('edit-user-account')

        else:
            messages.error(
                request, 'An error has occurred during registration')

    context = {
        'form': form
    }

    return render(request, 'users/login_signup.html', context)


@login_required(login_url="login")
def profile(request):
    profile = request.user.profile
    context = {'profile':profile}
    return render(request, 'users/profile.html', context)

@login_required(login_url="login")
def deleteUserAccount(request):

    if request.method == 'POST':
        id = request.user.id
        logout(request)
        User = get_user_model()
        User.objects.filter(id=id).delete()
        messages.success(request, 'You have deleted your CredKeep account.')
        return redirect('signup')

    return render(request, 'delete_template.html')
