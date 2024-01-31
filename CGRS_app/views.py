from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth import authenticate, login, logout
<<<<<<< HEAD
from django.contrib.auth.models import User
from CGRS_app.models import New_Reg
=======
from django.contrib.auth.forms import UserCreationForm
from .models import user_login,user_register,User
from django.db import IntegrityError

>>>>>>> 4a6d8bf4b0fc8507f20bc4bc2423618a4edc5069



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

def std_registration(request):
    return render(request,'std_registration.html')

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

<<<<<<< HEAD
# def user_Register(request):
#     if request.method=='POST':
#         RegNo=request.POST.get('Register_No')
#         Email=request.POST.get('email')
#         # if User.objects.filter(Register_No=RegNo).exists():
#         #     msg = 'Register Number already exists!'
#         #     return render(request, 'login.html',{'msg':msg})
#         # else:
           
#         Password=request.POST.get('password')
#         Confirm_password=request.POST.get('confirm_password')
            
#         # my_user=User.objects.create_user(RegNo,Email,Password)
#         # my_user.save()
#         # user1=User.objects.filter(Register_No=Register_No,password=password,email=email,confirm_password=confirm_password)
#         # for i in user1:
#         #         if i.Register_No==Register_No:
#         #             user=i.id
#         #             break
#         # user = User.objects.get(id=user)
#             # user_details.objects.create(user=user,Phone=phone,Qualification=qualification,Interest=interest)
#             # return redirect('success')
#         user=User(
#             username=RegNo,
#             email=Email,
#             password=Password
#         )  
#         user.save()

    return render(request, 'login.html')
=======
# def user_register(request):
#     if request.method=='POST':
#         username=request.POST['username']
#         if User.objects.filter(username=username).exists():
#             msg = 'Username already exists!'
#             return render(request, 'login.html',{'msg':msg})
#         else:
#             email=request.POST['email']
#             password=request.POST['password']
#             confirm_password=request.POST['confirm_passoword']
            
#             User.objects.create(username=username,email=email,password=password,confirm_password=confirm_password)
#             user1=User.objects.filter(username=username,password=password,email=email,confirm_password=confirm_password)
#             for i in user1:
#                 if i.Register_No==username:
#                     user=i.id
#                     break
#             user = User.objects.get(id=user)
#         return render(request, 'login.html')


def user_register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Check if passwords match
        if password != confirm_password:
            msg = 'Passwords do not match!'
            return render(request, 'login.html', {'msg': msg})

        try:
            # Create the user
            user = User.objects.create_user(username=username, email=email, password=password)
            # Additional check (if you have a 'Register_No' field in your model)
            if hasattr(user, 'Register_No') and user.Register_No == username:
                return render(request, 'login.html')
        except IntegrityError as e:
            msg = 'An error occurred. Please try again.'
            return render(request, 'login.html', {'msg': msg})
        except ValueError as e:
            msg = 'Invalid input. Please check your data and try again.'
            return render(request, 'login.html', {'msg': msg})

    return render(request, 'registration.html')

>>>>>>> 4a6d8bf4b0fc8507f20bc4bc2423618a4edc5069

def staff_reg(request):
    return render(request, 'staff_form.html')

def admin_reg(request):
    return render(request, 'testuser.html')

def newReg(request):
    if request.method == 'POST':
        namE = request.POST.get('Name')
        emaiL = request.POST.get('Email')
        reg_nO = request.POST.get('Reg_no')
        
        pasS = request.POST.get('Pass')

        my_user = User.objects.create_user(namE,emaiL,pasS)
        my_user.save()

        Regs = New_Reg(
            name = namE,
            email = emaiL,
            reg_no = reg_nO,
        )
        Regs.save()
        return redirect('index')   

    return render(request,'newreg.html')

