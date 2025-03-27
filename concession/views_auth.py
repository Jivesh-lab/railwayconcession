from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from concession.models import SignForm,details
from django.contrib import messages 
from datetime import datetime
import json
from django.http import JsonResponse

#Code for Sign up
def savedata(request):
    if request.method=="POST":
        username = request.POST.get('username')  # Fetching 'username' field
        email = request.POST.get('email1')  # Fetching 'email1' field
        password = request.POST.get('password1')
        data=SignForm(username=username,email=email,password=password)
        data.save()
    return render(request,'login.html')

# Code for saving Candidate details
def savedetail(request):
    if request.method=="POST":
        studname = request.POST.get('studentname')  # Fetching 'username' field
        clgname = request.POST.get('collegename')  # Fetching 'email1' field
        station1 = request.POST.get('station1')
        station2 = request.POST.get('station2')
        Class=request.POST.get('classes')
        validity=int(request.POST.get("month"))
        current = datetime.strptime(request.POST.get("current_date"), "%Y-%m-%d").date()
        valid_till = datetime.strptime(request.POST.get("valid_till_date"), "%Y-%m-%d").date()
        signform_instance = SignForm.objects.last() 
        print("Student Name:", studname)
        print("College Name:", clgname)
        print("Station 1:", station1)
        print("Station 2:", station2)
        print("Class:", Class)
        print("Validity:", validity)
        print("Current Date:", current)
        print("Valid Till Date:", valid_till)
        print("SignForm Instance:", signform_instance)
           
    if signform_instance:
            # Save details in the database
            detail = details(
                studentname=studname,
                collegename=clgname,
                station1=station1,
                station2=station2,
                travel_class=Class,
                validity=validity,
                current_date=current,
                valid_till_date=valid_till,
                login_id=signform_instance
            )
            detail.save()

            messages.success(request, "Your concession request has been submitted.")

            return redirect('home')  # Prevents form resubmission on refresh

    # Check if the user already has a concession
    user_has_concession = details.objects.filter(login_id=SignForm.objects.last()).exists()

    return render(request, 'concession2.html', {"user_has_concession": user_has_concession})


#Code for Login

    
def login_ajax(request):
    if request.method == "POST":
        data = json.loads(request.body)  # Get data from AJAX request
        email = data.get("email")
        password = data.get("password")
        print("Received Email:", email)
        print("Received Password:", password)
        try:
            user = SignForm.objects.get(email=email)  # Check if email exists
            if user.password == password: #  Verify password
                request.session["user_id"] = user.login_id  # Store user ID in session
                return JsonResponse({"success": True})  # Login success response
            else:
                return JsonResponse({"success": False, "error_type": "password", "message": "Incorrect password"})
        except SignForm.DoesNotExist:
            return JsonResponse({"success": False, "error_type": "email", "message": "Email not registered"})

    return JsonResponse({"error": "Invalid request"}, status=400)

