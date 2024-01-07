from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    return render(request, 'index.html')

def update_profile(request):
    return render(request,  'profile_update.html')

def update(request):
    if request.method == 'POST':
        profile_picture = request.POST['profile_picture']
        bio = request.POST['bio']
        skills = request.POST['skills']
        interests = request.POST['interests']
        portfolio_url = request.POST['portfolio_url']
        twitter_url = request.POST['twitter']
        linkedin_url = request.POST['linkedin']
        user = User.objects.update(profile_picture=profile_picture,
                                   bio=bio,
                                   skills=skills,
                                   interests=interests,
                                   portfolio_url=portfolio_url,
                                   twitter_url=twitter_url,
                                   linkedin_url=linkedin_url)
        user.save()
        return redirect('index')



def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('index') 
        else:
            messages.info(request, 'Username or Password not correct')
            return render(request, 'login.html')
    else:

        return render(request, 'login.html')


def signup(request):

    if request.method == 'POST':


        username = request.POST['username']
        email = request.POST['email']
        phone = request.POST['phone']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if User.objects.filter(username=username).exists():
            messages.info(request, 'Username is taken! Try something else')
            return redirect('signup')
        elif User.objects.filter(email=email).exists():
            messages.info(
                request, 'Email exists in the database, try Login or Forgot Password')
            return redirect('signup')
        elif password1 != password1:
            messages.info(request, 'Passwords doesn\'t match')
            return redirect('signup')
        else:
            user = User.objects.create_user(username=username,
                                            email=email,
                                            password=password1, 
                                            phone=phone)
            user.save()
  
            return redirect('login')
    else:
        return render(request, 'signup.html')


def logout_user(request):
    logout(request)
    return redirect('/')
