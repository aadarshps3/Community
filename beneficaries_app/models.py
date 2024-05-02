from django.db import models

from accounts.models import *

# Create your models here.
class Assistance(BaseModel):
    beneficiary = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    volunteer = models.ForeignKey(User,on_delete=models.CASCADE,related_name='vol_asst',null=True,blank=True)
    assistance_type = models.CharField(max_length=50,null=True,blank=True)
    required_amount = models.CharField(max_length=6,null=True,blank=True)
    assistance_details = models.TextField(null=True,blank=True)
    stat=(('Pending','Pending'),('Approved','Approved'),('Rejected','Rejected'))
    status=models.CharField(max_length=50,choices=stat,default='Pending',null=True)