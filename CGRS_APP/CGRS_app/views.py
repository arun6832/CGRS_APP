from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from CGRS_app.models import *

def index(request):
    return render(request, 'index.html')

from django.contrib import messages


#New Student Register
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
            my_user = User.objects.create_user(username=reg_no, email=email, password=password,)
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
    else:

        return render(request, 'newreg.html')

def HODReg(request):
    if request.method == 'POST':
        name = request.POST.get('Name')
        email = request.POST.get('Email')
        reg_no = request.POST.get('Reg_no')
        password = request.POST.get('Pass')

        try:
            # Check if a user with the given username (reg_no) already exists
            existing_user = User.objects.get(username=reg_no)
            msg = f"User with username {reg_no} already exists!"
            return render(request, 'HODreg.html', {'msg': msg})

        except User.DoesNotExist:
            # Create a new user if the username is unique
            my_user = User.objects.create_user(username=reg_no, email=email, password=password,is_superuser=True,is_staff=False)
            my_user.save()

            Regs = New_Reg(
                name=name,
                email=email,
                reg_no=reg_no,
            )
            Regs.save()

            return redirect('NEWLOGIN')

        except IntegrityError as e:
            # Handle other integrity errors
            msg = "Error creating user. Please try again!"
            return render(request, 'HODreg.html', {'msg': msg})
    else:

        return render(request, 'HODreg.html')
    
def StaffReg(request):
    if request.method == 'POST':
        name = request.POST.get('Name')
        email = request.POST.get('Email')
        reg_no = request.POST.get('Reg_no')
        password = request.POST.get('Pass')

        try:
            # Check if a user with the given username (reg_no) already exists
            existing_user = User.objects.get(username=reg_no)
            msg = f"User with username {reg_no} already exists!"
            return render(request, 'staffreg.html', {'msg': msg})

        except User.DoesNotExist:
            # Create a new user if the username is unique
            my_user = User.objects.create_user(username=reg_no, email=email, password=password,is_superuser=False,is_staff=True)
            my_user.save()

            Regs = New_Reg(
                name=name,
                email=email,
                reg_no=reg_no,
            )
            Regs.save()

            return redirect('NEWLOGIN')

        except IntegrityError as e:
            # Handle other integrity errors
            msg = "Error creating user. Please try again!"
            return render(request, 'staffreg.html', {'msg': msg})
    else:

        return render(request, 'staffreg.html')


#New Student Login (Checking and Logging in)
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

#student dashboard
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

#checkstatus of the complaint by the student
def student_checkst(request):
    return render(request,'student_checkstatus.html')

#logout of the student
def student_logout(request):
    return render(request,'mlogin.html')


#New Staff Register
def newStaff(request):
    if request.method == 'POST':
        name = request.POST.get('Name')
        email = request.POST.get('Email')
        reg_no = request.POST.get('Reg_no')
        password = request.POST.get('Pass')

        # try:
        #     # Check if a user with the given username (reg_no) already exists
        #     existing_user = User.objects.get(username=reg_no)
        #     msg = f"User with username {reg_no} already exists!"
        #     return render(request, 'staffreg.html', {'msg': msg})

        # except User.DoesNotExist:
        #     # Create a new user if the username is unique
        #     my_user = User.objects.create_user(username=reg_no, email=email, password=password)
        #     my_user.save()

        Regs = StaffReg(
            # user=my_user,
            name=name,
            email=email,
            reg_no=reg_no,
        )            
        Regs.save()

        return redirect('staff_login')

    # except IntegrityError as e:
    #     # Handle other integrity errors
    #     msg = "Error creating user. Please try again!"
    #     return render(request, 'staffreg.html', {'msg': msg})
    else:

        return render(request, 'staffreg.html')


def slogin(request):
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

    return render(request, 'staff_login.html')

def staff_dash(request):
    return render(request,'staff.html')

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


def staff_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username)

        try:
            staff_user = StaffReg.objects.get(username=username)
        except StaffReg.DoesNotExist:
            staff_user = None

        print(f"Username: {username}, Password: {password}")

        if staff_user and staff_user.password == password:
            user = staff_user.user
            authenticate_user = authenticate(request, username=username, password=password)

            print(f"Authenticate user: {authenticate_user}")

            if authenticate_user is not None:
                login(request, user)
                print("Login successful")
                return redirect('staff_dashboard')
            else:
                messages.error(request, 'Authentication failed.')
                print("Authentication failed")
        else:
            messages.error(request, 'Invalid login credentials.')
            print("Invalid login credentials.")

    return render(request, 'staff_login.html')

# def staffreg(request):
#     if request.method == 'POST':
#         register = request.POST.get('register')
#         password = request.POST.get('password')

#         print(f"Attempting login with username: {register}")

#         user = authenticate(username=register, password=password)
#         if user is not None:
#             login(request, user)
#             print("Login successful!")
#             return redirect('student_dash')
#         else:
#             print("Login failed. Invalid credentials.")
#             messages.error(request, 'Invalid username or password.')

#     return render(request, 'staffreg.html')

# def staff_dash(request):
#     return render(request, 'staff.html')

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def staff_after_login(request):
    return render(request, staff.html)

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

from django.db import IntegrityError

from .models import complaint  # Import the Complaint model

def NEWLOGIN(request):
    if request.method == 'POST':
        register1 = request.POST.get('register')
        password1 = request.POST.get('password')

        user = authenticate(username=register1, password=password1)
        print(user)
        if user is not None:
            if user.is_superuser==1 and user.is_staff==1:
                login(request, user)                                                                                                                            
                print("Login successful!")
                return redirect('admin_dashboard')

            elif user.is_superuser==1 and user.is_staff==0:
                login(request, user)                                                                                                                            
                print("Login successful!")
                return redirect('HODprofile')

            elif user.is_superuser==0 and user.is_staff==1:
                login(request, user)                                                                                                                            
                print("Login successful!")
                return redirect('staff_dashboard')

            elif user.is_superuser==0 and user.is_staff==0:
                login(request, user)                                                                                                                            
                print("Login successful!")
                return redirect('student_dashb')
        else:
            print("Login failed. Invalid credentials.")
            messages.error(request, 'Invalid username or password.')
    else:
        return render(request, 'NEWLOGIN.html')
    return render(request, 'NEWLOGIN.html')


def logout_views(request):
    logout(request)
    return redirect('index')