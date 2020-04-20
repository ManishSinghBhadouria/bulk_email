from .models import registration
from django.contrib.auth.models import User,auth
from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import logout
from random import randint
import smtplib
from django.core.mail import send_mail
from django.contrib import messages
import requests
from django.contrib.sessions.models import Session
from django.core.files.storage import FileSystemStorage

def index(request):
    if request.method == 'POST':
        pwd = request.POST['pwd']
        email = request.POST['email']
        context={'email':email,'pwd':pwd}
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        if server.login(email, pwd):
            return  render (request,'sendmail.html',context)
        else:
            messages.info(request, 'Invalid Credentials !!!!')
            return  render (request,'index.html')
        server.quit()
    return  render (request,'index.html')


def sendmail(request):
    if request.method == 'POST':
        pwd = request.POST['pwd']
        email = request.POST['email']
        programme = request.POST['programme']
        branch = request.POST['branch']
        sem = request.POST['sem']
        if registration.objects.filter(programme=programme).filter(branch=branch).filter(sem=sem):
            allrecord = registration.objects.filter(programme=programme).filter(branch=branch).filter(sem=sem).all()
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(email, pwd)
            msg = request.POST['msg']
            subject = request.POST['sub']
            body = "Subject: {}\n\n{}".format(subject,msg)
            for record in allrecord:
                email=record.email
                server.sendmail(email, email, body)
            server.quit()
        else:
            messages.info(request, 'Students Not Found !!!!')
            return redirect(index)
    messages.info(request, 'Send Successfully !!!!')
    return redirect(index)

def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        programme = request.POST['programme']
        branch = request.POST['branch']
        sem = request.POST['sem']
        subject='VIKRANT GROUP OF INSTITUTIONS'
        bod='Your Four Digits One Time Password OTP For Registration In VIKRANT BULK EMAIL SYSTEM Is--'
        otp= generate(4)
        message = f'{otp}'
        body= bod + str(otp)
        context={'name':name,'email':email,'programme':programme,'sem':sem,'branch':branch,'totp':otp}
        if registration.objects.filter(email=email).exists():
            messages.info(request, 'Email Already Exist !!!!')
            return redirect('register')
        else:
            send_mail(subject,body,'vikrantgroupofinstitutionsgwal@gmail.com',[email],fail_silently=False)
            return render(request,'password.html',context)
    else:
        return render(request,'register.html')

def generate(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

def validate(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        programme = request.POST['programme']
        branch = request.POST['branch']
        sem = request.POST['sem']
        otp = request.POST['otp']
        totp = request.POST['totp']
        if otp==totp:
            if registration.objects.filter(email=email).exists():
                    messages.info(request, 'Email Already Exist !!!!')
                    return redirect('register')
            user = registration(name=name,email=email, programme=programme, branch=branch, sem=sem)
            user.save()
            messages.info(request, 'Registered Successfully !!!!')
            return redirect('index')
        else:
            messages.info(request, 'OTP Is Not Correct !!!!')
            return redirect('validate')