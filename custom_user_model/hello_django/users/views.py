from django.shortcuts import redirect,render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import CustomUser
from datetime import datetime

# Create your views here.

def home(request):
    return render(request, "authentication/index.html")

def signup(request):

    if request.method == "POST":
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        birth_year = request.POST['birth_year']
        address = request.POST['address']

        # if birth_year:
        #     try:
        #         birth_year_int = int(birth_year)
        #     except ValueError:
        #         pass

        def calculate_age(birth_year):
            current = datetime.now().year
            return current - int(birth_year)

        age = calculate_age(birth_year)

        if password1 == password2:
            myuser = CustomUser.objects.create_user(username=username, email=email, password=password1)
            myuser.birth_year = birth_year 
            myuser.address = address
            myuser.age = age
            myuser.save()
            messages.success(request, "Your account has been successfully created.")
            return redirect('signin')
        else:
            messages.error(request, "Passwords do not match.")
            return render(request, "authentication/signup.html")

        messages.success(request, "Your account has been successfully created.")
        
        return redirect('signin')

    return render(request, "authentication/signup.html")

def signin(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password1']

        print(f"Username: {username}, Password: {password}")

        user = authenticate(request, username = username, password = password)
        print(user)
        if user is not None:
            login(request,user)
            return render(request, "authentication/index.html")
        else:
            messages.error(request, "Incorrect Credentials")
            return redirect('signin')
    return render(request, "authentication/signin.html")

def signout(request):

    logout(request)
    messages.success(request, "Logged Out Successfully!")
    return redirect('home')