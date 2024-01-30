from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import user_login,user_register,User



def index(request):
    return render(request, 'index.html')

# def user_login(request):
#     if request.method == 'POST':
#         register = request.POST.get('register')
#         password = request.POST.get('password')

#         print(f"Attempting login with username: {register}")

#         user = authenticate(username=register, password=password)
#         if user is not None:
#             login(request, user)
#             print("Login successful!")
#             return redirect('dashboard')
#         else:
#             print("Login failed. Invalid credentials.")
#             # Handle authentication failure, e.g., show an error message
#             pass

#     return render(request, 'login.html')  # Make sure to render the login page for GET requests

def HOD(request):
    return render(request,'HOD.html')

def HODprofile(request):
    return render(request,'HODprofile.html')

def HODtable(request):
    return render(request,'HODtable.html')

def std_form(request):   
    return render(request,'std_form.html')

def std_dashboard(request):
    return render(request,'std_dashboard.html')

def std_thankyou(request):
    return render(request,'std_thankyou.html')

def studentUsers(request):
    return render(request,'studentUsers.html')

def HODnot(request):
    return render(request,'HODnot.html')

def form(request):
    return render(request,'/student/form.html')

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None and user.is_active:
            if user.is_superuser==True and user.is_staff==True:
                login(request,user)
                return redirect('std_form')
            elif user.is_superuser==False and user.is_staff==False:
                login(request,user)
                return redirect('std_form')
        elif user is None:
            msg = "Wrong credentials. Please try again!"
            return render(request , 'login.html' , {'msg':msg})
    return render(request , 'login.html')

def user_register(request):
    if request.method=='POST':
        Register_No=request.POST['name']
        if User.objects.filter(Register_No=Register_No).exists():
            msg = 'Register Number already exists!'
            return render(request, 'login.html',{'msg':msg})
        else:
            email=request.POST['email']
            password=request.POST['password']
            confirm_password=request.POST['confirm_passoword']
            
            User.objects.create(Register_No=Register_No,email=email,password=password,confirm_password=confirm_password)
            user1=User.objects.filter(Register_No=Register_No,password=password,email=email,confirm_password=confirm_password)
            for i in user1:
                if i.Register_No==Register_No:
                    user=i.id
                    break
            user = User.objects.get(id=user)
            # user_details.objects.create(user=user,Phone=phone,Qualification=qualification,Interest=interest)
            # return redirect('success')
            
    return render(request, 'login.html')

