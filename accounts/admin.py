from django.contrib import admin
from .models import *

# Register your models here.


admin.site.register(CustomUser)
admin.site.register(StudentProfile)
admin.site.register(AdministratorProfile)
admin.site.register(Subscription)
admin.site.register(RequestDocument)
admin.site.register(Notification)
admin.site.register(ActivityLog)
