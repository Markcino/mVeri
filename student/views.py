from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from accounts.forms import FeedbackForm, RequestForm
from django.http import JsonResponse
from accounts.models import Feedback, RequestDocument, StudentProfile, AdministratorProfile
from django.contrib.auth.decorators import login_required

@login_required(login_url='do_login')
def student_dashboard(request):
    return render(request, "backend/student/index.html")

@login_required(login_url='do_login')
def request_document(request):
    current_user = request.user
    request_documents = RequestDocument.objects.all()


    context = {
        'current_user': current_user,
        'request_documents': request_documents,
    }
    
    return render(request, "backend/student/request_document.html", context)

@login_required(login_url='do_login')
def request_form(request):
    current_user = request.user
    student_profile = current_user.student_profile  # Get the StudentProfile instance
    institution_name = student_profile.school_name

    try:
        institution_profile = AdministratorProfile.objects.get(institution_name=institution_name)
    except AdministratorProfile.DoesNotExist:
        messages.error(request, "Institution not found.")
        return redirect("request-form")

    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            # Manually save the data to the Request model
            request_obj = RequestDocument.objects.create(
                student=student_profile,  # Adjust this to match your model's fields
                institution=institution_profile,
                sender_email=form.cleaned_data['requester_email'],
                doc_type = form.cleaned_data['doc_type'],
                request_date = form.cleaned_data['request_date'],
                purpose = form.cleaned_data['purpose'],
                is_pending = True,
                is_progress = False,
                is_approve = False,
                is_rejected = False,
            )
            request_obj.save()
            messages.success(request, "Request for Document Sent Successfully")
            return redirect("request-document")
        else:
            messages.error(request, "Your Request for Document Failed, Please Try Again")
    else:
        form = RequestForm(initial={
            'student': current_user.get_name(),
            'institution': institution_name,
            'requester_email': current_user.email
        })

    context = {
        'RequestForm': form,
        'current_user': current_user,
    }

    return render(request, "backend/student/request_form.html", context)
@login_required(login_url='do_login')
def request_history(request):
    return render(request, "backend/student/request_history.html")
@login_required(login_url='do_login')
def student_notifications(request):
    return render(request, "backend/student/notifications.html")
@login_required(login_url='do_login')
def help_support(request):
    return render(request, "backend/student/help_support.html")

def student_settings(request):
    return render(request, "backend/student/settings.html")
@login_required(login_url='do_login')
def student_feedback(request):

    current_user = request.user
    student_feedback = current_user.student_profile  # Get the StudentProfile instance
    institution_name = student_feedback.school_name

    try:
        institution_profile = AdministratorProfile.objects.get(institution_name=institution_name)
    except AdministratorProfile.DoesNotExist:
        messages.error(request, "Institution not found.")
        return redirect("request-form")
    
    if request.method == 'POST':
        pass
    else:
        form = FeedbackForm(initial={
            'student': current_user.get_name,
        })
    
    context = {
        'FeedBackForm': form,
        'current_user': current_user,
    }
    return render(request, "backend/student/feedback.html", context)


@login_required(login_url='do_login')
def student_profile(request):
    return render(request, "backend/student/profile.html")

@login_required(login_url='do_login')
def update_profile(request):
    pass