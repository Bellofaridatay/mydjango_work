from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import detail
from django.contrib.auth.models import User, auth
from django.contrib import messages



# Create your views here.

def index(request):

    return render(request,'index.html')


def register(request):

    if request.method == 'POST':

        uname = request.POST['uname']
        email = request.POST['email']
        pword = request.POST['pword']
        cpword = request.POST['cpword']
        dept = request.POST['dept']

        if pword == cpword:

            if User.objects.filter(username=uname).exists():
                messages.info(request, uname + ', already exist, Try another Username!!!')
                return redirect('register')

            elif User.objects.filter(email=email).exists():
                messages.info(request, email + ', already exist, Try another Email Address!!!')
                return redirect('register')

            else:
                user = User.objects.create_user(username=uname, email=email, password=pword)
                lg = detail.objects.create(uname=uname, dept=dept)
                user.save()
                lg.save()
                return redirect('signin')
                
        else:
            messages.info(request, 'Password does not match!!!')
            return redirect('register')
    else:
        return render(request,'register.html')

def signin(request):   
    if request.method == 'POST':

        uname = request.POST['uname']
        pword = request.POST['pword']

        user = auth.authenticate(username=uname, password=pword)

        if user is not None:
            auth.login(request, user)
            return redirect('.')

        else:
            messages.info(request, 'Invalid Login Details!!!')
            return redirect('signin')


    else:
        return render(request,'signin.html')








