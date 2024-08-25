# student/urls.py
from django.urls import path
from . import views
from accounts.utils import hash_url 
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path(f'student_dashboard/{hash_url("student_dashboard")}', views.student_dashboard, name="student-dashboard"),
    path(f'student_request_document/{hash_url("student_request_document")}', views.request_document, name="request-document"),
    path(f'request_form/{hash_url("request_form")}', views.request_form, name="request-form"),


    path(f'request_history/{hash_url("request_history")}', views.request_history, name="request-history"),
    path(f'student_notifications/{hash_url("student_notifications")}', views.student_notifications, name="student-notifications"),
    path(f'help_support/{hash_url("help_support")}', views.help_support, name="help-support"),
    path(f'student_settings/{hash_url("student_settings")}', views.student_settings, name="student-settings"),
    path(f'student_feedback/{hash_url("student_feedback")}', views.student_feedback, name="student-feedback"),
    path(f'student_profile/{hash_url("student_profile")}', views.student_profile, name="student-profile"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
