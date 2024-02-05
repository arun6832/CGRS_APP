from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from matplotlib import pyplot as plt

from django.shortcuts import render , redirect
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.models import User
from Christcourier.models import CustomUser, P_Details,New_staff,New_admin

def index(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        pass1 = request.POST.get('pass')

        print(username,pass1)
        
        # Check if password matches for a specific user
        user = authenticate(request, username=username, password=pass1)
        
        print(user)
        
        if user is not None:
            # Check user role and redirect accordingly
            if user.is_superuser:
                print('hi')
                login(request, user)
                return redirect('admin_db')
            elif user.is_staff or user.user_type == 'staff':
                login(request, user)
                return redirect("sdashboard")
            else:
                login(request, user)
                return redirect('dashboard')
        else:
            # Handle invalid credentials
            return render(request, "user/index.html", {'error_message': 'Invalid credentials'})

    # If it's a GET request or other cases, return a response (e.g., render the login page)
    return render(request, "user/index.html")

        

def service(request):
    return render(request,"user/service.html")

def about(request):  
    return render(request,"user/about.html")

def contact(request):
    return render(request,"user/contact.html")

def reci(request):
    return render(request,"user/dashboard.html")

def register(request):
    if request.method == 'POST':
        user_type = request.POST.get('choice', 'user') 

        Email = request.POST.get('Email')
        Name = request.POST.get('Name')
        Phone_Number = request.POST.get('Phone_Number')
        reg_Number = request.POST.get('Reg_No')
        pass1 = request.POST.get('pass')

        my_user = CustomUser.objects.create(username=Email,email=Email,password=pass1,first_name=Name,user_type=user_type,phone=Phone_Number,
            reg_no=reg_Number)


        # Regs=CustomUser(email=Email,
        # name=Name,
        # phone=Phone_Number,
        # reg_no=reg_Number)
        # Regs.save()
        return redirect('index')    
    return render(request,"user/reg.html")

def receive(request):
    
    if request.method=="POST":
        Id = request.POST.get('parcelId')
        email = request.POST.get('recEmail')
        Recname = request.POST.get('recName')
        Recphone = request.POST.get('recContact')  # Assuming recContact is the correct name
        Deldate = request.POST.get('delDate')
        Company = request.POST.get('company')
        
        add=P_Details(
            rec_id=Id,
            rec_email=email,
            rec_name=Recname,
            rec_phone=Recphone,
            reg_date=Deldate,
            rec_company=Company
        )
        add.save()
        # data = add.save()
        # if data:
    #         print("save")
    #     else:
    #         print("no") 
    # else:
    #     print("Not in Cond")           

    return render(request,"user/receive.html")

def dashboard(request):
    return render(request,"user/dashboard.html")

def stafflogin(request):
    if request.method == 'POST':
        EmaiL = request.POST.get('emaiL')
        Pass1 = request.POST.get('pasS')
        staff = authenticate(request,username=EmaiL,password=Pass1)
        if user is not None:
            login(request,staff)
            return redirect('sdashboard')
        else:
            return render(request,"staff/stafflogin.html")
    return render(request,"staff/stafflogin.html")

def staffreg(request):
    if request.method=='POST':
        NAME=request.POST.get('name')
        EMAIL=request.POST.get('email')
        PASS=request.POST.get('passwoard')

        Staff=New_staff(
            s_name=NAME,
            s_email=EMAIL
        )
        Staff.save()
        data = Staff.save()
        if data:
            print("save")

        else:
            print("NOOOOOO")                
        return redirect('sdashboard')

    return render(request,"staff/staffreg.html")

def sdashboard(request):
    return render(request,"staff/sdashboard.html")
def pstatus(request):
    return render(request,"staff/pstatus.html")

def admin_db(request):
    return render(request,"admin/admin_db.html")

def recipient_(request):
   
    details=P_Details.objects.all()
    return render(request,"admin/recipient_.html",{'parcel':details})

def adminreg(request):
    if request.method=='POST':
        N=request.POST.get('a_n')
        E=request.POST.get('a_e')

        Ad = New_admin(
            a_name=N,
            a_email=E
        )
        Ad.save()
        data1 = Ad.save()
        if data1:
            print("save")

        else:
            print("ooooO")                
        return redirect('admin/adminlog.html')
        
    return render(request,"admin/adminreg.html")

def adminlog(request):
    if request.method == 'POST':
        Ne = request.POST.get('em')
        Pw = request.POST.get('pw')
        admin_ =  authenticate(request,username=Ne,password=Pw)
        if user is not None:
            login(request,admin_)
            return redirect('admin_db')

        else:
            return render(request,"admin/adminlog.html")
    return render(request,"admin/adminlog.html")
def plot_graph(request):
    # Retrieve data from the database
    data = P_Details.objects.values('reg_date', 'rec_company')

    # Extract data for plotting
    dates = [entry['reg_date'] for entry in data]
    companies = [entry['rec_company'] for entry in data]

    # Create a plot
    plt.figure(figsize=(10, 6))
    plt.scatter(dates, companies)
    plt.title('Registration Date vs Company')
    plt.xlabel('Registration Date')
    plt.ylabel('Company')
    plt.xticks(rotation=45)

    # Save the plot to a BytesIO object
    from io import BytesIO
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    
    # Clear the plot for the next use
    plt.clf()

    # Convert the BytesIO object to base64 for embedding in HTML
    import base64
    plot_image = base64.b64encode(buffer.read()).decode('utf-8')

    # Pass the base64 image to the template
    return render(request, 'admin/dash.html', {'plot_image': plot_image})