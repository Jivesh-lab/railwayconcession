from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from concession.models import SignForm,details
from django.contrib import messages

def login(request):
    if request.session.get("user_id"):  # Check if user is already logged in
        return redirect("home") 
    return render(request, 'login.html')

def homepage(request):
    if not request.session.get("user_id"):  # If user is not logged in
        return redirect("login") 
    return render(request, 'home.html')

def myform(request):
    
    # 1️⃣ Get user ID from session (since you're not using Django's auth system)
    user_id = request.session.get("user_id")  # Assuming you store user ID in session
    print(f" DEBUG: Logged-in user ID from session = {user_id}")

    # 2️⃣ Check if user ID exists in the session
    if not user_id:
        print(" ERROR: No user ID found in session!")
        return render(request, "concession2.html", {"user_has_concession": False})

    # 3️⃣ Check if the user has applied for a railway concession
    concession_exists = details.objects.filter(login_id=user_id).exists()
    print(f"DEBUG: user_has_concession = {concession_exists}")

    # 4️⃣ Render template with the correct context
    return render(request, "concession2.html", {"user_has_concession": concession_exists})


def myadmin(request):
    return render(request, 'myadmin.html')

def settings(request):
    return render(request, 'setting.html')

def status(request):
    return render(request, 'status.html')

def logout(request):
    request.session.flush()  # Clear all session data (logs user out)
    return redirect("login")  # Redirect to login page after logout
 
#Logic for checking validity of pass
