from django.db import models
from .managers import CustomUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

# Create your models here.

class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    t_and_c = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('staff'), default=False)
    is_superuser = models.BooleanField(_('superuser'), default=False)
    is_student = models.BooleanField(_('student'), default=False)
    is_administrator = models.BooleanField(_('administrator'), default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    @property
    def get_name(self):
        return self.first_name + " " + self.last_name

    def __str__(self):
        return self.email


class StudentProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='student_profile')
    school_name = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    institution_code = models.CharField(max_length=50, blank=True, null=True)
    class_name = models.CharField(max_length=50, blank=True, null=True)
    degree_type = models.CharField(max_length=50, blank=True, null=True)
    graduation_date = models.DateField(blank=True, null=True)
    is_completed = models.BooleanField(default=False)
    is_incomplete = models.BooleanField(default=True)

    @property
    def get_institution_name(self):
        return self.school_name

    def __str__(self):
        return f"{self.user.get_name} - Student Profile"


class AdministratorProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='administrator_profile')
    institution_name = models.CharField(max_length=255, blank=True, null=True)
    institution_address = models.CharField(max_length=255, blank=True, null=True)
    institution_code = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    business_reg_number = models.CharField(max_length=50, blank=True, null=True)
    business_cert = models.FileField(upload_to='certificates/', blank=True, null=True)
    institution_code = models.CharField(max_length=50, blank=True, null=True)
    is_completed = models.BooleanField(default=False)
    is_incomplete = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.institution_name} - Administrator Profile"


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


class RequestDocument(models.Model):
    DOC_TYPE_CHOICES = [
        ('None', 'None'),
        ('Degree', 'Degree'),
        ('diploma', 'Diploma'),
        ('certificate', 'Certificate'),
        ('transcript', 'Transcript'),
        ('recommendation_letter', 'Recommendation Letter'),
    ]
    
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    institution = models.ForeignKey(AdministratorProfile, on_delete=models.CASCADE)
    doc_type = models.CharField(max_length=50, choices=DOC_TYPE_CHOICES, default='None')
    request_date = models.DateField(default=timezone.now)
    is_pending = models.BooleanField(default=True)
    is_progress = models.BooleanField(default=False)
    is_approve = models.BooleanField(default=False)
    is_rejected = models.BooleanField(default=False)
    sender_email = models.EmailField()
    purpose = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"Transcript Request by {self.student.user.get_name}"


class Notification(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Notification for {self.student.user.get_name}"


class SchoolNotice(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class ActivityLog(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Activity for {self.student.user.get_name}"


class Feedback(models.Model):
    RATING_CHOICES = [
        (1, '1 Star'),
        (2, '2 Stars'),
        (3, '3 Stars'),
        (4, '4 Stars'),
        (5, '5 Stars'),
    ]
    
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, related_name='feedbacks')
    review_text = models.TextField()
    rating = models.IntegerField(choices=RATING_CHOICES)
    school_rating = models.IntegerField(choices=RATING_CHOICES)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Feedback by {self.student.user.get_name} - {self.rating} Stars"
