from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from accounts.models import AdministratorProfile, StudentProfile, CustomUser, RequestDocument

# Create your views here.
@login_required(login_url='do_login')
def school_admin_dashboard(request):
    return render(request, "backend/school_administrator/index.html")

def all_document_request(request):
    current_user = request.user
    all_document_requests = RequestDocument.objects.filter(
        is_pending=True, 
        institution=current_user.administrator_profile
    ).order_by('-request_date')
    print(all_document_request)

    context = {
        'all_document_requests': all_document_requests,
    }
    return render(request, "backend/school_administrator/all_document_request.html", context)