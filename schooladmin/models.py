from django.db import models

from accounts.models import AdministratorProfile, StudentProfile

# Create your models here.

class TranscriptGenerated(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    institution = models.ForeignKey(AdministratorProfile, on_delete=models.CASCADE)
    graduation_year = models.CharField(max_length=4)
    requested_date = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    grade_10 = models.DecimalField(max_digits=5, decimal_places=2)
    grade_11 = models.DecimalField(max_digits=5, decimal_places=2)
    grade_12 = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.student.user.get_name}"
