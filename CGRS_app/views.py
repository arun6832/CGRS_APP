from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from CGRS_app.models import New_Reg



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

def studentGreivance(request):
    return render(request,'studentGreivance.html')

def studentReports(request):
    return render(request,'studentReports.html')

def studentUsers(request):
    return render(request,'studentUsers.html')

def HODnot(request):
    return render(request,'HODnot.html')

def form(request):
    return render(request,'/student/form.html')

def user_login(request):
    if request.method == "POST":
        Register_No = request.POST.get('Register_No')
        password = request.POST.get('password')
        print(Register_No,password)
        user = authenticate(request,username=Register_No,password=password)
        print(user)
        if user is not None and user.is_active:
            if user.is_superuser==False and user.is_staff==True:
                login(request,user)
                return redirect('dashboard')
            elif user.is_superuser==False and user.is_staff==False:
                login(request,user)
                return redirect('dashboard')
        elif user is None:
            msg = "Wrong credentials. Please try again!"
            return render(request , 'login.html' , {'msg':msg})
    return render(request , 'login.html')

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

def staff_reg(request):
    return render(request, 'staff_form.html')

def admin_reg(request):
    return render(request, 'testuser.html')

def testdashboard(request):
    return render(request,'testdashboard.html')

def testgrievance(request):
    return render(request,'testgrievances.html')

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

