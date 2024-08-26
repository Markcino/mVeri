from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from accounts.models import AdministratorProfile, StudentProfile, CustomUser, RequestDocument

# Create your views here.
@login_required(login_url='do_login')
def school_admin_dashboard(request):
    current_user = request.user
    all_document_requests = RequestDocument.objects.filter(
        is_pending=True, 
        institution=current_user.administrator_profile
    ).order_by('-request_date')
    print(all_document_request)

    context = {
        'all_document_requests': all_document_requests,
    }
    return render(request, "backend/school_administrator/index.html", context)

def all_document_request(request):
    current_user = request.user
    all_document_requests = RequestDocument.objects.filter(
        is_pending=True, 
        institution=current_user.administrator_profile
    ).order_by('-request_date')

    context = {
        'all_document_requests': all_document_requests,
    }
    return render(request, "backend/school_administrator/all_document_request.html", context)


def upload_document(request, request_document_id):
    # Get the current user (administrator)
    current_user = request.user

    # Get the specific document request
    document_request = get_object_or_404(RequestDocument, id=request_document_id, institution=current_user.administrator_profile)
    

    # Retrieve the student and their class
    student_profile = document_request.student
    student_name = student_profile.user.get_name
    student_email = student_profile.user.email
    graduation_date = student_profile.graduation_date
    class_name = student_profile.class_name.lower()  
    request_date = document_request.request_date

    # Define class categories in lowercase
    junior_classes = [
        'k-i', 'k-ii', '1st grade', '2nd grade', '3rd grade', '4th grade', 
        '5th grade', '6th grade', '7th grade', '8th grade', '9th grade', 
        '10th grade', '11th grade'
    ]
    senior_high_graduate = ['12th grade']
    university_graduate = [
        'undergraduate degree', 'master degree', 'phd'
    ]

    # Check the class name (now case-insensitive) and render the appropriate template
    if class_name in junior_classes:
        return render(request, "backend/school_administrator/elem_junior.html", {
            'student_name': student_name,
            'student_email': student_email,
            'graduation_date': graduation_date,
            'request_date': request_date,
        })
    elif class_name in senior_high_graduate:
        return render(request, "backend/school_administrator/high_school_graduate.html", {
            'student_name': student_name,
            'student_email': student_email,
            'request_date': request_date,
        })
    elif class_name in university_graduate:
        return render(request, "backend/school_administrator/university_graduate.html", {
            'student_name': student_name,
            'student_email': student_email,
            'graduation_date': graduation_date,
            'request_date': request_date,
        })

    return redirect('all_document_request')


@login_required(login_url='do_login')
def school_admin_help_support(request):
    return render(request, "backend/school_administrator/help_support.html")

@login_required(login_url='do_login')
def school_admin_notifications(request):
    return render(request, "backend/school_administrator/notifications.html")


def school_admin_settings(request):
    return render(request, "backend/school_administrator/settings.html")


@login_required(login_url='do_login')
def school_admin_profile(request):
    return render(request, "backend/school_administrator/profile.html")