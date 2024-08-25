from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('super-admin-dashboard', views.app_administrator_dashboard,
         name="super-admin-dashboard"),

    # School Administrator Urls
    path('all-school-admin', views.school_administrator_list,
         name="school_admin_list"),
    path('create-school-admin', views.superadmin_create_school_administrator,
         name="create_school_admin"),
    path('edit-school-admin/<int:pk>', views.superadmin_edit_school_administrator,
         name="edit_school_admin"),
    path('delete-school-admin/<int:pk>', views.superadmin_delete_school_administrator,
         name="delete_school_admin"),
    # End of School Administrator Urls

    # Student Urls
    path('all-student', views.superadmin_student_list,
         name="student_list"),
    path('create-student', views.superadmin_create_student,
         name="create_student"),
    path('edit-student/<int:pk>', views.superadmin_edit_student,
         name="edit_student"),
    path('delete-student/<int:pk>', views.superadmin_delete_student,
         name="delete_student"),
    # End of Student Urls
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)