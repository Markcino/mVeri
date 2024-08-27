import json

from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from accounts.models import AdministratorProfile, StudentProfile, CustomUser, RequestDocument, TranscriptGenerated

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
    institution_name = current_user.administrator_profile.institution_name
    institution_address = current_user.administrator_profile.institution_address
    phone_number = current_user.administrator_profile.phone_number

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
            'institution_name': institution_name,
            'institution_address': institution_address,
            'phone_number': phone_number,
        })
    elif class_name in senior_high_graduate:
        return render(request, "backend/school_administrator/high_school_graduate.html", {
            'student_name': student_name,
            'student_email': student_email,
            'graduation_date': graduation_date,
            'request_date': request_date,
            'institution_name': institution_name,
            'institution_address': institution_address,
            'phone_number': phone_number,
        })
    elif class_name in university_graduate:
        return render(request, "backend/school_administrator/university_graduate.html", {
            'student_name': student_name,
            'student_email': student_email,
            'graduation_date': graduation_date,
            'request_date': request_date,
            'institution_name': institution_name,
            'institution_address': institution_address,
            'phone_number': phone_number,
        })

    return redirect('all_document_request')

def create_transcript(request):
    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        student = request.POST.get('student')
        institution = request.POST.get('institution')
        graduation_year = request.POST.get('graduation_year')
        requested_date = request.POST.get('requested_date')
        subject = request.POST.get('subject')
        grade_10_average = request.POST.get('grade_10_average')
        grade_11_average = request.POST.get('grade_11_average')
        grade_12_average = request.POST.get('grade_12_average')
        grade_10_conduct = request.POST.get('grade_10_conduct')
        grade_11_conduct = request.POST.get('grade_11_conduct')
        grade_12_conduct = request.POST.get('grade_12_conduct')
        registrar_signed = request.POST.get('registrar_signed') == 'on'
        principal_approved = request.POST.get('principal_approved') == 'on'
        table_data = request.POST.get('table_data')

        # Convert the JSON string to a list of dictionaries
        table_data = json.loads(table_data)

        transcript = TranscriptGenerated.objects.create(
            student=student,
            institution=institution,
            graduation_year=graduation_year,
            requested_date=requested_date,
            subject=subject,
            grade_10_average=grade_10_average,
            grade_11_average=grade_11_average,
            grade_12_average=grade_12_average,
            grade_10_conduct=grade_10_conduct,
            grade_11_conduct=grade_11_conduct,
            grade_12_conduct=grade_12_conduct,
            registrar_signed=registrar_signed,
            principal_approved=principal_approved
        )

        # Save the table data to the database
        for row_data in table_data:
            TranscriptGenerated.objects.create(
                subject=row_data['subject'],
                grade_10=row_data['grade_10'],
                grade_11=row_data['grade_11'],
                grade_12=row_data['grade_12'],
                transcript=transcript,
            )

        return JsonResponse({'success': True})

    return JsonResponse({'success': False})

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