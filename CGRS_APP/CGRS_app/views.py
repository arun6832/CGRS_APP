from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from CGRS_app.models import New_Reg

def index(request):
    return render(request, 'index.html')

from django.contrib import messages

def mlogin(request):
    if request.method == 'POST':
        register = request.POST.get('register')
        password = request.POST.get('password')

        print(f"Attempting login with username: {register}")

        user = authenticate(username=register, password=password)
        if user is not None:
            login(request, user)
            print("Login successful!")
            return redirect('student_dash')
        else:
            print("Login failed. Invalid credentials.")
            messages.error(request, 'Invalid username or password.')

    return render(request, 'mlogin.html')

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

# def mlogin(request):
#     if request.method == "POST":
#         Register_No = request.POST.get('Register_No')
#         password = request.POST.get('password')
#         print(Register_No,password)
#         user = authenticate(request,username=Register_No,password=password)
#         print(user)
#         if user is not None and user.is_active:
#             if user.is_superuser==False and user.is_staff==True:
#                 login(request,user)
#                 return redirect('dashboard')
#             elif user.is_superuser==False and user.is_staff==False:
#                 login(request,user)
#                 return redirect('dashboard')
#         elif user is None:
#             msg = "Wrong credentials. Please try again!"
#             return render(request , 'mlogin.html' , {'msg':msg})
#     return render(request , 'mlogin.html')

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

    # return render(request, 'login.html')

def staff_reg(request):
    return render(request, 'staff_login.html')

def admin_reg(request):
    return render(request, 'admin_login.html')

from .models import New_Reg, complaint

def admin_dash(request):
    try:
        # Fetch all complaints from the database
        all_complaints = complaint.objects.all()
        return render(request, 'testdashboard.html', {'complaints': all_complaints})
    except complaint.DoesNotExist:
        # Handle the case when there are no complaints
        return render(request, 'testdashboard.html', {'complaints': None})

def admin_students(request):
    try:
        # Fetch all new registration from the database
        all_registrations = New_Reg.objects.all()
        print(all_registrations)
        return render(request, 'teststudents.html', {'registrations': all_registrations})
    except New_Reg.DoesNotExist:
        # Handle the case when there are no complaints
        return render(request, 'teststudents.html', {'registrations': None})
# def newReg(request):
#     if request.method == 'POST':
#         namE = request.POST.get('Name')
#         emaiL = request.POST.get('Email')
#         reg_nO = request.POST.get('Reg_no')
        
#         pasS = request.POST.get('Pass')

#         my_user = User.objects.create_user(namE,emaiL,pasS)
#         my_user.save()

#         Regs = New_Reg(
#             name = namE,
#             email = emaiL,
#             reg_no = reg_nO,
#         )
#         Regs.save()
#         return redirect('index')   

#     return render(request,'newreg.html')

from django.db import IntegrityError

def newReg(request):
    if request.method == 'POST':
        name = request.POST.get('Name')
        email = request.POST.get('Email')
        reg_no = request.POST.get('Reg_no')
        password = request.POST.get('Pass')

        try:
            # Check if a user with the given username (reg_no) already exists
            existing_user = User.objects.get(username=reg_no)
            msg = f"User with username {reg_no} already exists!"
            return render(request, 'newreg.html', {'msg': msg})

        except User.DoesNotExist:
            # Create a new user if the username is unique
            my_user = User.objects.create_user(username=reg_no, email=email, password=password)
            my_user.save()

            Regs = New_Reg(
                name=name,
                email=email,
                reg_no=reg_no,
            )
            Regs.save()

            return redirect('mlogin')

        except IntegrityError as e:
            # Handle other integrity errors
            msg = "Error creating user. Please try again!"
            return render(request, 'newreg.html', {'msg': msg})

    return render(request, 'newreg.html')

from .models import complaint  # Import the Complaint model

def student_dashb(request):
    if request.method == 'POST':
        c_name = request.POST.get('c_name')
        c_email = request.POST.get('c_email')
        c_reg_no = request.POST.get('c_registerNumber')
        c_department = request.POST.get('c_department')
        c_complaint = request.POST.get('c_complaint')
        # c_image = request.POST.get('c_proof')
        
        # Use the correct model name
        complaint_data = complaint(
            reg_no=c_reg_no,
            email=c_email,
            name=c_name,
            department=c_department,
            complaint=c_complaint,
            image=request.FILES.get('c_proof')
        )

        complaint_data.save()

        return redirect('index')

    return render(request,'student_dashboard.html')


def student_checkst(request):
    return render(request,'student_checkstatus.html')

def student_logout(request):
    return render(request,'mlogin.html')


