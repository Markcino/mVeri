from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='do_login')
def app_administrator_dashboard(request):
    return render(request, "backend/superadmin/index.html")


# School Administrator views
@login_required(login_url='do_login')
def school_administrator_list(request):
    return render(request, "backend/superadmin/school_admin/school_admin_list.html")

@login_required(login_url='do_login')
def superadmin_create_school_administrator(request):
    return render(request, "backend/superadmin/school_admin/create_school_admin.html")

@login_required(login_url='do_login')
def superadmin_edit_school_administrator(request, pk):
    pass

@login_required(login_url='do_login')
def superadmin_delete_school_administrator(request, pk):
    pass

# End of School Administrator views

# Student views

@login_required(login_url='do_login')
def superadmin_student_list(request):
    return render(request, "backend/superadmin/student/student_list.html")

@login_required(login_url='do_login')
def superadmin_create_student(request):
    return render(request, "backend/superadmin/student/create_student.html")

@login_required(login_url='do_login')
def superadmin_edit_student(request, pk):
    pass

@login_required(login_url='do_login')
def superadmin_delete_student(request, pk):
    pass
# End of Student views