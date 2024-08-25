from django.contrib import messages
from django.shortcuts import render, redirect
from accounts.forms import TranscriptRequestForm

from django.http import JsonResponse
from accounts.models import StudentProfile, AdministratorProfile

def autocomplete_student(request):
    term = request.GET.get('term', '')
    students = StudentProfile.objects.filter(name__icontains=term).values_list('name', flat=True)
    return JsonResponse(list(students), safe=False)

def autocomplete_institution(request):
    term = request.GET.get('term', '')
    institutions = AdministratorProfile.objects.filter(institution_name__icontains=term).values_list('institution_name', flat=True)
    return JsonResponse(list(institutions), safe=False)

def get_user_data(request):
    if request.user.is_authenticated:
        user = request.user
        user_data = {
            'name': user.get_name,
            'institution': ''  # Default empty value
        }
        
        if user.is_administrator:
            admin_profile = getattr(user, 'administrator_profile', None)
            if admin_profile:
                user_data['institution'] = getattr(admin_profile, 'institution_name', '')
        
        if user.is_student:
            student_profile = getattr(user, 'student_profile', None)
            if student_profile:
                user_data['institution'] = getattr(student_profile, 'institution_name', '')
        
        print(user_data)
        return JsonResponse(user_data)
    else:
        return JsonResponse({'error': 'User not authenticated'}, status=401)

    
    


def student_dashboard(request):
    return render(request, "backend/student/index.html")

def request_document(request):
    current_user = request.user

    context = {
        'current_user': current_user,
    }
    
    return render(request, "backend/student/request_document.html", context)

def request_transcript_form(request):
    current_user = request.user
    form = TranscriptRequestForm()

    print(current_user)

    if request.method == "POST":
        form = TranscriptRequestForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Transcript Requested Successfully")
            return redirect("request-transcript")
        else:
            messages.error(request, "Transcript Request Failed, Please Try Again")
            return redirect("request-transcript")
    else:
        form = TranscriptRequestForm()
    
    context = {
        'TranscriptRequestForm': form,
        'current_user': current_user,
    }



    return render(request, "backend/student/request_transcript_form.html", context)

def request_history(request):
    return render(request, "backend/student/request_history.html")

def student_notifications(request):
    return render(request, "backend/student/notifications.html")

def help_support(request):
    return render(request, "backend/student/help_support.html")

def student_settings(request):
    return render(request, "backend/student/settings.html")

def student_feedback(request):
    return render(request, "backend/student/feedback.html")



def student_profile(request):
    return render(request, "backend/student/profile.html")

def update_profile(request):
    pass