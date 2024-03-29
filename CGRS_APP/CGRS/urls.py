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
from CGRS_app.views import *

urlpatterns = [
    path('admin/',admin.site.urls),
    path('', index, name='index'),
    path('logout', logout_views, name='logout'),
    # path('signup',user_Register,name='register'),
    path('HOD',HOD,name='HOD'),
    path('HODprofile',HODprofile,name='HODprofile'),
    path('HODtable',HODtable,name='HODtable'),
    path('HODnot',HODnot,name='HODnot'),
    path('std_form',std_form,name='std_form'),
    path('studentGreivance',studentGreivance,name='studentGreivance'),
    path('studentReports',studentReports,name='studentReports'),
    path('studentUsers',studentUsers,name='studentUsers'),
    path('staff_login',staff_login,name='staff_login'),
    path('admin_login',admin_reg,name='admin_form'),
    path('newReg',newReg,name='newReg'),
    path('mlogin',mlogin,name='mlogin'),
    path('student_dashboard',student_dashb,name='student_dashb'),
    path('student_checkstatus',student_checkst,name='student_staus'),
    path('mlogin',student_logout,name='student_log_out'),
    path('testdashboard',admin_dash,name='admin_dashboard'),
    path('teststudents',admin_students,name='admin_student_list'),
    path('staff',staff_dash,name='staff_dashboard'),
    path('Staffreg',StaffReg,name='StaffReg'),
    path('NEWLOGIN',NEWLOGIN,name='NEWLOGIN'),
    path('HODreg',HODReg,name='HODreg'),
]


