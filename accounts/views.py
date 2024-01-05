from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.


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
