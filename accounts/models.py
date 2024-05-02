from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser,PermissionsMixin
# Create your models here.
class BaseModel(models.Model):
    """Model for subclassing."""
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    updated_on = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True
        ordering = ['-created_on']

class UserManager(BaseUserManager):        
    def create_user(self, is_active=True,username=None,email=None, password=None,role=None, uid=None):
        
        if not username:
            raise ValueError('User must have an username')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            is_active=is_active, 
            role=role,
            uid=uid,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, password, email=None,role=None,uid=None):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
            role=1,
            uid=uid,
            )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True 
        user.save(using=self._db)
        return user
    
SELECTROLE = ((1, "admin"), (2, "volunteers"), (3, "beneficiaries"),(4,"fundraiser"))

class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=50, blank=True, null=True)
    username = models.CharField(max_length=50, unique=True, null=True)
    email = models.EmailField(max_length=100, null=True)
    role = models.IntegerField(choices=SELECTROLE)
    uid = models.CharField(max_length=500, unique=True, null=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_registered = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'username'
    
    REQUIRED_FIELDS=[]

    objects = UserManager()

    def __str__(self):
        return self.username
    class Meta:
        db_table = "user"

class UserProfile(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=25,blank=True, null=True)
    mobile_number = models.CharField(max_length=25,unique=True, null=True)
    availability = models.CharField(max_length=20, blank=True, null=True)
    profile_picture = models.ImageField(upload_to="volunteer_profiles/", blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    area = models.CharField(max_length=25,blank=True, null=True)
    date = models.DateField(auto_now=True)
    description = models.TextField(max_length=300,null=True,blank=True)

class WelfareProgram(BaseModel):
    volunteer = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=100,null=True,blank=True)
    venue = models.CharField(max_length=50,null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    start_date = models.DateField(null=True,blank=True)
    end_date = models.DateField(null=True,blank=True)
    stat=(('Pending','Pending'),('Accepted','Accepted'),('On Duty','On Duty'),('Rejected','Rejected'))
    status=models.CharField(max_length=50,choices=stat,default='Pending',null=True)




class Resource(BaseModel):
    name = models.CharField(max_length=100,null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    quantity = models.IntegerField(null=True,blank=True)

class Donation(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    donation_type = models.CharField(max_length=50,null=True,blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

class Fund(BaseModel):
    fund_name = models.CharField(max_length=100,null=True, blank=True)
    total_amount = models.DecimalField(max_digits=12, decimal_places=2,null=True, blank=True)
    allocated_amount = models.DecimalField(max_digits=12, decimal_places=2,null=True, blank=True)
    remaining_amount = models.DecimalField(max_digits=12, decimal_places=2,null=True, blank=True)

class ResourceAllocation(BaseModel):
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE,null=True, blank=True)
    allocation_type = models.CharField(max_length=50,null=True, blank=True)  # e.g., program-specific, beneficiary-specific
    allocated_quantity = models.IntegerField(null=True, blank=True)
    allocation_date = models.DateField(null=True, blank=True)

class ResourceReport(BaseModel):
    report_name = models.CharField(max_length=100,null=True, blank=True)
    report_content = models.TextField(null=True, blank=True)
    generation_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.report_name
    
class surveyquestions(BaseModel):
    question = models.CharField(max_length=200)