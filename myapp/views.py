from django.shortcuts import render, redirect
from .forms import signupForm, notesForm
from .models import usersignup
from django.contrib.auth import logout
from django.contrib import messages
from django.core.mail import send_mail
from batchproject import settings
import random


# Create your views here.


def index(request):
    if request.method == 'POST':  # root
        if request.POST.get('signup') == 'signup':
            username = ""
            newuser = signupForm(request.POST)
            if newuser.is_valid():
                username = newuser.cleaned_data.get('username')
                try:
                    un = usersignup.objects.get(username=username)
                    print("username is already exists!")
                    messages.error(request, "username is already exists!")
                except usersignup.DoesNotExist:
                    newuser.save()
                print("User created successfully!")
                messages.success(request, "User created successfully!")

                # Email Sending Code
                # send_mail(subject="Welcome!",message=f"Hello User!\nYour account has been created with us!\nEnjoy our services\n\nIf need any help, contact on\n+91987654321 | help@notesapp.com",from_email=settings.EMAIL_HOST_USER,recipient_list=["angelraninga0206@icloud.com"])
                # otp = random.randint(1111, 9999)
                sub = "Welcome!"
                msg = "Hello User!\nYour account has been created with us!\nEnjoy our services\nIf need any help, contact on\n+91987654321 | help@notesapp.com"
                from_ID = settings.EMAIL_HOST_USER
                to_ID = [request.POST['username']]
                send_mail(subject=sub, message=msg, from_email=from_ID, recipient_list=to_ID)
                return redirect('notes')
            else:
                print(newuser.errors)
        elif request.POST.get('login') == 'login':
            unm = request.POST['username']
            pas = request.POST['password']

            user = usersignup.objects.filter(username=unm, password=pas)
            uid = usersignup.objects.get(username=unm)
            print("UserID:", uid.id)
            if user:  # true
                print("Login Successfull!")
                request.session['user'] = unm
                request.session['userid'] = uid.id
                return redirect('notes')
            else:
                print("Error! Username or Password does't match.")
    return render(request, 'index.html')


def notes(request):
    user = request.session.get('user')
    uid = request.session.get('userid')
    if request.method == 'POST':
        mynote = notesForm(request.POST, request.FILES)
        if mynote.is_valid():
            mynote.save()
            print("Your notes has been uploaded!")
        else:
            print(mynote.errors)
    return render(request, 'notes.html', {'user': user, 'cuser': usersignup.objects.get(id=uid)})


def userlogout(request):
    logout(request)
    return redirect('/')


def updateprofile(request):
    user = request.session.get('user')
    uid = request.session.get('userid')
    cuser = usersignup.objects.get(id=uid)
    if request.method == 'POST':
        updateuser = signupForm(request.POST)
        if updateuser.is_valid():
            updateuser = signupForm(request.POST, instance=cuser)
            updateuser.save()
            print('Your profile has been updated!')
            return redirect('notes')
        else:
            print(updateuser.errors)
    return render(request, 'updateprofile.html', {'user': user, 'cuser': usersignup.objects.get(id=uid)})


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')
