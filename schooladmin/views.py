from datetime import datetime
import json
from decimal import Decimal, InvalidOperation
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from accounts.models import AdministratorProfile, StudentProfile, CustomUser, RequestDocument 
from .models import TranscriptGenerated

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
    class_name = student_profile.class_name 
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
    if request.method == 'POST':
        student_name = request.POST.get('student')
        institution_name = request.POST.get('institution')
        graduation_year = request.POST.get('graduation_year')
        requested_date = request.POST.get('requested_date')
        
        table_data = json.loads(request.POST.get('table_data'))

        # Get the related student and institution profiles
        student = get_object_or_404(StudentProfile, user__first_name__icontains=student_name.split()[0], 
                                    user__last_name__icontains=student_name.split()[1])
        institution = get_object_or_404(AdministratorProfile, institution_name=institution_name)

        # Track created subjects to prevent duplicates
        created_subjects = set()

        # Validate and save each row of table data
        for row in table_data:
            subject = row.get('subject', '')
            grade_10 = row.get('grade_10', '')
            grade_11 = row.get('grade_11', '')
            grade_12 = row.get('grade_12', '')

            try:
                grade_10 = Decimal(grade_10) if grade_10 else None
                grade_11 = Decimal(grade_11) if grade_11 else None
                grade_12 = Decimal(grade_12) if grade_12 else None
            except InvalidOperation:
                return JsonResponse({'error': 'Invalid decimal value in grades'}, status=400)

            # Create a unique identifier for the transcript entry
            transcript_identifier = (student, institution, graduation_year, subject)

            if transcript_identifier not in created_subjects:
                created_subjects.add(transcript_identifier)
                TranscriptGenerated.objects.create(
                    student=student,
                    institution=institution,
                    graduation_year=graduation_year,
                    requested_date=requested_date,
                    subject=subject,
                    grade_10=grade_10,
                    grade_11=grade_11,
                    grade_12=grade_12,
                )
        
        return JsonResponse({'message': 'Transcript saved successfully!'})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)


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