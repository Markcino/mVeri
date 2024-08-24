from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

def register(request):
    return render(request, "backend/account/register.html")
def login(request):
    try:
        form = AuthenticationForm()
        if request.method == "POST":
            form = AuthenticationForm(request, data=request.POST)

            if form.is_valid():
                username = request.POST.get('username')
                password = request.POST.get('password')

                user = authenticate(
                    request, username=username, password=password)

                if user is not None and user.is_active and user.is_administrator:
                    login(request, user)
                    messages.success(request, f"Welcome, {user.get_username()}!")

                    return redirect('administrator-dashboard')
                elif user is not None and user.is_active and user.is_student:
                    login(request, user)
                    messages.success(request, f"Welcome, {user.get_username()}!")

                    return redirect('student-dashboard')
                elif user is not None and user.is_active and user.is_superuser:
                    login(request, user)
                    messages.success(request, f"Welcome, {user.get_username()}!")

                    return redirect('admin-dashboard')
                else:
                    # Handle invalid user or insufficient privileges
                    messages.error(
                        request, "Invalid credentials or insufficient privileges")
                    return redirect('index')

            else:
                # Handle form validation errors
                errors = form.errors.as_json()
                return HttpResponse(errors, status=400)

        context = {'LoginForm': form}

        return render(request, "backend/account/login.html", context)
    except Exception as e:
        # Handle any other exceptions
        return HttpResponse("An error occurred: {}".format(str(e)))

    # if request.method == "POST":
    #     form = AuthenticationForm(request, data=request.POST)
    #     if form.is_valid():
    #         email = form.cleaned_data.get('username')
    #         password = form.cleaned_data.get('password')
    #         user = authenticate(request, username=email, password=password)

    #         if user is not None:
    #             login(request, user)
    #             messages.success(request, f"Welcome, {user.get_username()}!")
                
    #             # Check if the user has the `is_administrator` attribute
    #             if getattr(user, 'is_administrator', False):
    #                 return redirect('administrator_dashboard')
    #             elif getattr(user, 'is_worker', False):
    #                 return redirect('employee_dashboard')
    #             else:
    #                 # Handle users without specific roles
    #                 messages.warning(request, "You do not have access to an administrator or worker dashboard.")
    #                 return redirect('home')  # Redirect to a default or general dashboard
    #         else:
    #             messages.error(request, "Invalid credentials.")
    #     else:
    #         messages.error(request, "Please correct the errors below.")
    # else:
    #     form = AuthenticationForm()

    # context = {'LoginForm': form}
    # return render(request, "backend/account/login.html", context)


# User Logout View
@login_required(login_url='do_login')
def logout(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")

    return redirect('home')
