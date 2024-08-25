from django.shortcuts import render

# Create your views here.

def student_dashboard(request):
    return render(request, "backend/student/index.html")

def request_transcript(request):
    return render(request, "backend/student/request_transcript.html")

def request_letter(request):
    return render(request, "backend/student/request_letter.html")

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