from django.db import models
from . managers import CustomUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _



# Create your models here.

class CustomUser(AbstractBaseUser, PermissionsMixin):
    username:None
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    t_and_c = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('staff'), default=False)
    is_superuser = models.BooleanField(_('superuser'), default=False)
    is_student = models.BooleanField(_('student'),
        default=False)
    is_administrator = models.BooleanField(_('administrator'),
        default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    @property
    def get_name(self):
        return self.first_name+" "+self.last_name

    def __str__(self):
        return self.email

class StudentProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='student_profile')
    school_name = models.CharField(max_length=255, blank=True, null=True)
    class_name = models.CharField(max_length=50, blank=True, null=True)
    degree_type = models.CharField(max_length=50, blank=True, null=True)
    graduation_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.get_name} - Student Profile"

class AdministratorProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='administrator_profile')
    institution_name = models.CharField(max_length=255, blank=True, null=True)
    institution_address = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    business_reg_number = models.CharField(max_length=50, blank=True, null=True)
    business_cert = models.FileField(upload_to='certificates/', blank=True, null=True)

    def __str__(self):
        return f"{self.user.get_name} - Administrator Profile"
    
class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='profile_pics', blank=True, null=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}  Profile'


class Subscription(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, unique=True)
    
    subscription_id = models.CharField(max_length=300)
    subscriber_name = models.CharField(max_length=300)

    subscription_plan = models.CharField(max_length=255)
    subscription_cost = models.CharField(max_length=255)

    is_active = models.BooleanField(default=False)

    subscription_date = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return f'{self.subscriber_name} - {self.subscription_plan} subscription'  