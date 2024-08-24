from django.shortcuts import render

# Create your views here.

def app_administrator_dashboard(request):
    return render(request, "backend/superadmin/index.html")


# School Administrator views
def school_administrator_list(request):
    return render(request, "backend/superadmin/school_admin/school_admin_list.html")

def superadmin_create_school_administrator(request):
    return render(request, "backend/superadmin/school_admin/create_school_admin.html")

def superadmin_edit_school_administrator(request, pk):
    pass

def superadmin_delete_school_administrator(request, pk):
    pass

# End of School Administrator views

# Student views

def superadmin_student_list(request):
    return render(request, "backend/superadmin/student/student_list.html")

def superadmin_create_student(request):
    return render(request, "backend/superadmin/student/create_student.html")

def superadmin_edit_student(request, pk):
    pass

def superadmin_delete_student(request, pk):
    pass
# End of Student views