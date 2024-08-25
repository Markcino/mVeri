# student/urls.py
from django.urls import path
from . import views
from accounts.utils import hash_url 


# urlpatterns_data = [
#     ('student_dashboard', views.student_dashboard, name="student-dashboard"),  # Update name here
# ]

urlpatterns = [
    path(f'student_dashboard/{hash_url("student_dashboard")}', views.student_dashboard, name="student-dashboard"),
    path(f'student_request_transaction/{hash_url("student_request_transaction")}', views.request_transcript, name="request-transcript"),
    path(f'request_letter/{hash_url("request_letter")}', views.request_letter, name="request-letter"),
    path(f'request_history/{hash_url("request_history")}', views.request_history, name="request-history"),
    path(f'student_notifications/{hash_url("student_notifications")}', views.student_notifications, name="student-notifications"),
    path(f'help_support/{hash_url("help_support")}', views.help_support, name="help-support"),
    path(f'student_settings/{hash_url("student_settings")}', views.student_settings, name="student-settings"),
    path(f'student_feedback/{hash_url("student_feedback")}', views.student_feedback, name="student-feedback"),
    path(f'student_profile/{hash_url("student_profile")}', views.student_profile, name="student-profile"),
]
