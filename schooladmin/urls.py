from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('school_admin_dashboard', views.school_admin_dashboard,
         name="school-admin-dashboard"),
    path('all_document_request', views.all_document_request, name="all_document_request"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)