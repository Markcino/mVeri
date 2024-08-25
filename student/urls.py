# student/urls.py
from django.urls import path
from . import views
from accounts.utils import hash_url 


# urlpatterns_data = [
#     ('student_dashboard', views.student_dashboard, name="student-dashboard"),  # Update name here
# ]

urlpatterns = [
    path(f'student_dashboard/{hash_url("student_dashboard")}', views.student_dashboard, name="student-dashboard"),
    path(f'student_request_document/{hash_url("student_request_document")}', views.request_document, name="request-document"),
    path(f'request_transcript_form/{hash_url("request_transcript_form")}', views.request_transcript_form, name="request-transcript-form"),
    path(f'request_history/{hash_url("request_history")}', views.request_history, name="request-history"),
    path(f'student_notifications/{hash_url("student_notifications")}', views.student_notifications, name="student-notifications"),
    path(f'help_support/{hash_url("help_support")}', views.help_support, name="help-support"),
    path(f'student_settings/{hash_url("student_settings")}', views.student_settings, name="student-settings"),
    path(f'student_feedback/{hash_url("student_feedback")}', views.student_feedback, name="student-feedback"),
    path(f'student_profile/{hash_url("student_profile")}', views.student_profile, name="student-profile"),
    path(f'update_profile/{hash_url("update_profile")}', views.update_profile, name="update-profile"),
    path('autocomplete_student/', views.autocomplete_student, name='autocomplete-student'),
    path('autocomplete_institution/', views.autocomplete_institution, name='autocomplete-institution'),
    path('get_user_data/', views.get_user_data, name='get-user-data'),

]
