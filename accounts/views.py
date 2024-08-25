import datetime
from django.db import transaction, IntegrityError
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
import random
from django.core.files.storage import FileSystemStorage

from accounts.models import AdministratorProfile, CustomUser, StudentProfile

def generate_institution_code():
    prefix = "002-MV-"
    
    # Find the latest institution code
    latest_code = AdministratorProfile.objects.filter(
        institution_code__startswith=prefix
    ).order_by('-institution_code').first()
    
    # Determine the latest sequential parts
    if latest_code:
        parts = latest_code.institution_code.split('-')
        first_part = int(parts[-2])
        second_part = int(parts[-1])
        if second_part < 999:
            next_second_part = second_part + 1
            next_code = f"{prefix}{first_part:03d}-{next_second_part:03d}"
        else:
            next_first_part = first_part + 1
            next_code = f"{prefix}{next_first_part:03d}-001"
    else:
        next_code = f"{prefix}001-001"
    
    return next_code

def register(request):
    institution_search = AdministratorProfile.objects.filter(is_incomplete=False, is_completed=True)
    institution_names = [institution.institution_name for institution in institution_search]

    if request.method == 'POST':
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        is_student = request.POST.get('isStudent')
        is_administrator = request.POST.get('isSchoolAdmin')
        accept_terms = request.POST.get('acceptTerms')

        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return render(request, 'backend/account/register.html', {'institution_names': institution_names})

        if not accept_terms:
            messages.error(request, "You must accept the Terms and Conditions.")
            return render(request, 'backend/account/register.html', {'institution_names': institution_names})

        if is_student and is_administrator:
            messages.error(request, "You cannot select both Student and School Administrator.")
            return render(request, 'backend/account/register.html', {'institution_names': institution_names})

        if not is_student and not is_administrator:
            messages.error(request, "You must select either Student or School Administrator.")
            return render(request, 'backend/account/register.html', {'institution_names': institution_names})

        with transaction.atomic():
            user = CustomUser(
                email=email,
                first_name=first_name,
                last_name=last_name,
                password=make_password(password1),
                is_student=bool(is_student),
                is_administrator=bool(is_administrator),
                t_and_c=True,
            )
            user.save()

            is_complete = True
            is_incomplete = False
            institution_code = None  # Initialize the variable

            if is_student:
                graduation_date_str = request.POST.get('graduation_date')
                if graduation_date_str:
                    graduation_date_str += '-01'
                    try:
                        graduation_date = datetime.datetime.strptime(graduation_date_str, '%Y-%m-%d').date()
                    except ValueError:
                        messages.error(request, "Invalid graduation date format.")
                        return render(request, 'backend/account/register.html', {'institution_names': institution_names})
                else:
                    graduation_date = None

                school_name = request.POST.get('school_name')
                class_name = request.POST.get('class')
                degree_type = request.POST.get('degree_type')

                try:
                    admin_profile = AdministratorProfile.objects.get(institution_name=school_name)
                    institution_code = admin_profile.institution_code
                except AdministratorProfile.DoesNotExist:
                    messages.error(request, "Invalid institution name.")
                    return render(request, 'backend/account/register.html', {'institution_names': institution_names})

                if not all([school_name, class_name, degree_type, graduation_date]):
                    is_complete = False
                    is_incomplete = True

                student_profile = StudentProfile(
                    user=user,
                    school_name=school_name,
                    class_name=class_name,
                    degree_type=degree_type,
                    graduation_date=graduation_date,
                    institution_code=institution_code,
                    is_completed=is_complete,
                    is_incomplete=is_incomplete
                )
                student_profile.save()

            elif is_administrator:
                institution_name = request.POST.get('institution_name')
                institution_address = request.POST.get('institution_address')
                phone_number = request.POST.get('phone_number')
                business_reg_number = request.POST.get('business_reg_number')
                business_cert = request.FILES.get('business_cert', None)

                if not all([institution_name, institution_address, phone_number, business_reg_number, business_cert]):
                    is_complete = False
                    is_incomplete = True

                institution_code = generate_institution_code()

                admin_profile = AdministratorProfile(
                    user=user,
                    institution_name=institution_name,
                    institution_address=institution_address,
                    institution_code=institution_code,
                    phone_number=phone_number,
                    business_reg_number=business_reg_number,
                    business_cert=business_cert,
                    is_completed=is_complete,
                    is_incomplete=is_incomplete
                )
                admin_profile.save()

        messages.success(request, 'Registration successful!')
        return redirect('do_login')

    context = {
        "institution_names": institution_names,
    }
    return render(request, "backend/account/register.html", context)


# User Login View
def do_login(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None and user.is_active and user.is_superuser:
                login(request, user)
                messages.success(request, f"Welcome, {user.get_username()}!")
                return redirect('super-admin-dashboard')

            if user is not None and user.is_active and user.is_administrator:
                login(request, user)
                messages.success(request, f"Welcome, {user.get_username()}!")
                return redirect('school-admin-dashboard')

            if user is not None and user.is_active and user.is_student:
                login(request, user)
                messages.success(request, f"Welcome, {user.get_username()}!")
                return redirect('student-dashboard')

            else:
                messages.error(request, "Invalid credentials or insufficient privileges")
                return redirect('index')

        else:
            errors = form.errors.as_json()
            return HttpResponse(errors, status=400)

    context = {'LoginForm': form}
    return render(request, "backend/account/login.html", context)

# User Logout View
@login_required(login_url='do_login')
def do_logout(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")

    return redirect('index')
