from django.db import models

class (models.Model):
    pid=models.IntegerField(primary_key=True)
    pname = models.CharField(max_length=30)
    pcontactno = models.CharField(max_length=12)
    pemail=models.CharField(max_length=40)
    sid=models.ForeignKey(service,on_delete=models.CASCADE)
    pstatus=models.BooleanField()
    
    def _str_(self):
        return str(self.pname._str_())
# Create your models here.
