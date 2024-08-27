from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('school_admin_dashboard', views.school_admin_dashboard,
         name="school-admin-dashboard"),
    path('all_document_request', views.all_document_request, name="all_document_request"),
    path('upload_document/<int:request_document_id>/', views.upload_document, name="upload_document"),
    path('create_transcript', views.create_transcript, name="create_transcript"),
    path('school_admin_help_support', views.school_admin_help_support, name="help_support"),
    path('school_admin_settings', views.school_admin_settings, name="admin_settings"),
    path('school_admin_profile', views.school_admin_profile, name="admin_profile"),
    path('school_admin_notifications', views.school_admin_notifications, name="admin_notifications"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)