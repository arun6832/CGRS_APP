"""
URL configuration for CGRS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.contrib import admin
<<<<<<< HEAD
from CGRS_app.views import index,HOD,HODprofile,HODtable,HODnot, user_login,std_form,studentGreivance,studentReports,studentUsers,staff_reg, admin_reg,newReg,std_login
=======
from CGRS_app.views import *
>>>>>>> 8701c588fbf8796b57fdf40022cb00e0a8612db2

urlpatterns = [
    path('admin/',admin.site.urls),
    path('', index, name='index'),
    path('login', user_login, name='login'),
    # path('signup',user_Register,name='register'),
    path('HOD',HOD,name='HOD'),
    path('HODprofile',HODprofile,name='HODprofile'),
    path('HODtable',HODtable,name='HODtable'),
    path('HODnot',HODnot,name='HODnot'),
    path('std_form',std_form,name='std_form'),
    path('studentGreivance',studentGreivance,name='studentGreivance'),
    path('studentReports',studentReports,name='studentReports'),
    path('studentUsers',studentUsers,name='studentUsers'),
    path('staff_form',staff_reg,name='staff_form'),
<<<<<<< HEAD
    path('test_user',admin_reg,name='admin_reg'),
    path('newReg',newReg,name='newReg'),
    path('login',std_login,name='student_login')
=======
    path('testdashboard',testdashboard,name='testdashboard'),
    path('testgrievances',testgrievance,name='testgrievances'),
    path('testuser',testuser,name='testuser'),
    path('testreports',testreports,name='testreports'),
    path('newReg',newReg,name='newReg'),
    path('admin_login',admin_login,name='admin_login'),
>>>>>>> 8701c588fbf8796b57fdf40022cb00e0a8612db2
]


