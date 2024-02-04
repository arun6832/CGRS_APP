from django.contrib import admin
from .models import New_Reg, complaint
# Register your models here.
class userAdmin(admin.ModelAdmin):
    list_display=('name','reg_no','email','c_password','password')
admin.site.register(New_Reg,userAdmin)

class complaintAdmin(admin.ModelAdmin):
    list_display=('reg_no','email','name','complaint','image')
admin.site.register(complaint,complaintAdmin)