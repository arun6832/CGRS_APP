from django.db import models
from django.contrib.auth.models import User

class user_register(models.Model):
    Register_No=models.ForeignKey(User,on_delete=models.CASCADE,default=0)
    email=models.CharField(max_length=100,null=False)
    password=models.CharField(max_length=100,null=False)
    confirm_password=models.CharField(max_length=100,null=True)

class user_login(models.Model):
      Register_No=Register_No=models.ForeignKey(User,on_delete=models.CASCADE,default=0)
      password=password=models.CharField(max_length=100,null=False)
class Meta:
        app_label = 'CGRS_app'