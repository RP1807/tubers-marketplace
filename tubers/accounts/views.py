from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(request=request, username=username, password=password)

        if user is not None:
            auth.login(request=request, user=user)
            messages.success(request=request, message="You are logged in")
            return redirect(to="dashboard")
        else:
            messages.warning(request=request, message="Invalid credentials")
            return redirect(to='login')
    return render(request=request, template_name="accounts/login.html")


def register(request):
    if request.method == "POST":
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request=request, message="Username already exists")
                return redirect(to='register')

            if User.objects.filter(email=email).exists():
                messages.error(request=request, message="Email already exists")
                return redirect(to='register')

            try:
                user = User.objects.create_user(username=username, first_name=firstname, last_name=lastname,
                                                email=email, password=password)
                user.save()
                messages.success(request=request, message="Account created successfully")
                return redirect(to='login')
            except Exception as ex:
                print(ex)
                messages.warning(request=request, message="Failed to save user")
                return redirect(to='register')
        else:
            messages.warning(request=request, message="Password and Confirm password are different")
            return redirect(to='register')

    return render(request=request, template_name="accounts/register.html")


def logout_user(request):
    logout(request)
    return redirect(to="login")


@login_required(login_url='login')
def dashboard(request):
    return render(request=request, template_name="accounts/dashboard.html")
