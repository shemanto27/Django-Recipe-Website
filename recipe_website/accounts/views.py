from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def registration(request):
    if request.method == 'POST':
        data = request.POST
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        user = User.objects.filter(username=username)
        if user.exists():
            messages.info(request, 'username already exists!')
            return redirect('/registration')

        user = User.objects.create(  
            username=username,
            email=email,
        )
        user.set_password(password)
        user.save()
        messages.info(request, 'User registered successfully!')
        return redirect('/login') 
    context = {'page_title': 'Registration Page'}
    return render(request, "registration.html", context)

def login_page(request):
    if request.method == 'POST':
        data = request.POST
        username = data.get('username')
        password = data.get('password')
        
        if not User.objects.filter(username = username).exists():
            messages.error(request,"User Does not Exists!")
            return redirect('/login')
        else:
            user = authenticate(username = username, password = password)
            if user is None:
                messages.error(request, "Password Incorrect")
                return redirect('/login')
            else:
                login(request, user)
                return redirect('/all_recipes')
    context = {'page_title': 'Login Page'}  
    return render(request, "login.html", context)

def logout_page(request):
    logout(request)
    return redirect('/login')
