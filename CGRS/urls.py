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
from CGRS_app.views import index, user_register,HOD,HODprofile,HODtable,HODnot, user_login,std_form,std_dashboard,std_thankyou,std_registration

urlpatterns = [
    path('admin/',admin.site.urls),
    path('', index, name='index'),
    path('login', user_login, name='login'),
    path('signup',user_register,name='register'),
    path('HOD',HOD,name='HOD'),
    path('HODprofile',HODprofile,name='HODprofile'),
    path('HODtable',HODtable,name='HODtable'),
    path('HODnot',HODnot,name='HODnot'),
    path('std_form',std_form,name='std_form'),
    path('std_dashboard',std_dashboard,name='std_dashboard'),
    path('std_thankyou',std_thankyou,name='std_thankyou'),
    path('std_registration',std_registration,name='std_registration')
]


