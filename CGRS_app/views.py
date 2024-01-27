from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


def index(request):
    return render(request, 'index.html')

def user_login(request):
    if request.method == 'POST':
        register = request.POST.get('register')
        password = request.POST.get('password')

        print(f"Attempting login with username: {register}")

        user = authenticate(username=register, password=password)
        if user is not None:
            login(request, user)
            print("Login successful!")
            return redirect('dashboard')
        else:
            print("Login failed. Invalid credentials.")
            # Handle authentication failure, e.g., show an error message
            pass

    return render(request, 'login.html')  # Make sure to render the login page for GET requests

def HOD(request):
    return render(request,'HOD.html')

def HODprofile(request):
    return render(request,'HODprofile.html')

def HODtable(request):
    return render(request,'HODtable.html')

def dashboard(request):
    return render(request,'dashboard.html')

def HODnot(request):
    return render(request,'HODnot.html')