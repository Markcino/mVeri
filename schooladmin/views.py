from django.shortcuts import render

# Create your views here.

def school_admin_dashboard(request):
    return render(request, "backend/school_administrator/index.html")