from django.db import models
from django.contrib.auth.models import User

<<<<<<< HEAD

class New_Reg(models.Model):
        reg_no=models.CharField(max_length=200)
        email=models.CharField(max_length=100)
        name=models.CharField(max_length=200)
        password=models.CharField(max_length=100,null=False)
        c_password=models.CharField(max_length=100,null=True)
=======
class user_register(models.Model):
    username=models.ForeignKey(User,on_delete=models.CASCADE,default=0)
    email=models.CharField(max_length=100,null=False)
    password=models.CharField(max_length=100,null=False)
    confirm_password=models.CharField(max_length=100,null=True)
    
class user_login(models.Model):
      Register_No=Register_No=models.ForeignKey(User,on_delete=models.CASCADE,default=0)
      password=password=models.CharField(max_length=100,null=False)
class Meta:
        app_label = 'CGRS_app'
>>>>>>> 4a6d8bf4b0fc8507f20bc4bc2423618a4edc5069
