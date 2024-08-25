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

from accounts.models import AdministratorProfile, CustomUser, StudentProfile

def register(request):
    if request.method == 'POST':
        # Get the form data from the request
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        is_student = request.POST.get('isStudent')
        is_administrator = request.POST.get('isSchoolAdmin')
        accept_terms = request.POST.get('acceptTerms')

        # Validate the form data
        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return render(request, 'registration_form.html')

        if not accept_terms:
            messages.error(request, "You must accept the Terms and Conditions.")
            return render(request, 'registration_form.html')

        if is_student and is_administrator:
            messages.error(request, "You cannot select both Student and School Administrator.")
            return render(request, 'registration_form.html')

        if not is_student and not is_administrator:
            messages.error(request, "You must select either Student or School Administrator.")
            return render(request, 'registration_form.html')

        try:
            # Start a transaction
            with transaction.atomic():
                # Create the user
                user = CustomUser(
                    email=email,
                    first_name=first_name,
                    last_name=last_name,
                    password=make_password(password1),  # Hash the password
                    is_student=bool(is_student),
                    is_administrator=bool(is_administrator),
                    t_and_c=True,  # Terms accepted
                )
                user.save()  # Save the user to the database

                # Create the appropriate profile based on the user's role
                if is_student:
                    # Extract and convert the graduation_date
                    graduation_date_str = request.POST.get('graduation_date')
                    if graduation_date_str:
                        # Append '-01' to make it a full date (YYYY-MM-DD)
                        graduation_date_str += '-01'
                        try:
                            # Convert the string to a valid date
                            graduation_date = datetime.datetime.strptime(graduation_date_str, '%Y-%m-%d').date()
                        except ValueError:
                            messages.error(request, "Invalid graduation date format.")
                            return render(request, 'registration_form.html')
                    else:
                        graduation_date = None  # Handle case where no graduation date is provided

                    # Create the student profile
                    student_profile = StudentProfile(
                        user=user,
                        school_name=request.POST.get('school_name'),
                        class_name=request.POST.get('class'),
                        degree_type=request.POST.get('degree_type'),
                        graduation_date=graduation_date  # Save the valid graduation date
                    )
                    student_profile.save()

                elif is_administrator:
                    admin_profile = AdministratorProfile(
                        user=user,
                        institution_name=request.POST.get('institution_name'),
                        institution_address=request.POST.get('institution_address'),
                        phone_number=request.POST.get('phone_number'),
                        business_reg_number=request.POST.get('business_reg_number'),
                        business_cert=request.FILES.get('business_cert')
                    )
                    admin_profile.save()

            # If everything is successful, commit the transaction and show a success message
            messages.success(request, 'Registration successful!')
            return redirect('do_login')  # Redirect to the login page

        except IntegrityError:
            # If there is any error, roll back the transaction and show an error message
            messages.error(request, "There was an error with the registration. Please try again.")
            return render(request, 'registration_form.html')

    # If the request method is GET, render the registration form
    return render(request, "backend/account/register.html")

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
