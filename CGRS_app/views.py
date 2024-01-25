from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


def index(request):
    return render(request, 'index.html')

def user_login(request):
    if request.method == 'POST':
        register = request.POST['register']
        password = request.POST['password']
        user = authenticate(username=register, password=password)
        if user is not None:
            login(request, user)
            return redirect('admin-dashboard')
        else:
            # Handle authentication failure
            pass
    return render(request,'login.html')

def admin(request):
    return render(request,'admin.html')