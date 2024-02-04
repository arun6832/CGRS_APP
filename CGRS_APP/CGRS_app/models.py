from django.db import models
from django.contrib.auth.models import User


class New_Reg(models.Model):
        reg_no=models.CharField(User,max_length=200)
        email=models.CharField(max_length=100)
        name=models.CharField(max_length=200)
        password=models.CharField(max_length=100,null=False)
        c_password=models.CharField(max_length=100,null=True)

class complaint(models.Model):
    reg_no = models.CharField(User,max_length=200, null=True, blank=True)
    email = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    department = models.CharField(max_length=100)
    complaint = models.CharField(max_length=10000)
    image = models.ImageField(upload_to='complaint_proof/')

        # def __str__(self):
        #         return f"{self.}"