from subprocess import PIPE
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import user_data
from django.contrib.auth.models import User, auth
from django.contrib import messages



# Create your views here.

def index(request):

    return render(request,'index.html')


def register(request):

    if request.method == 'POST':

        name = request.POST['name']
        uname = request.POST['uname']
        email = request.POST['email']
        pword = request.POST['pword']
        cpword = request.POST['cpword']

        if pword == cpword:

            if user_data.objects.filter(uname=uname).exists():
                messages.info(request, uname + ', already exist, Try another Username!!!')
                return redirect('register')

            elif user_data.objects.filter(email=email).exists():
                messages.info(request, email + ', already exist, Try another Email Address!!!')
                return redirect('register')

            else:
                user_data.objects.create(uname=uname, email=email, pword=pword, name=name).save()
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

        user = auth.authenticate(uname=uname, pword=pword)

        if user is not None:
            auth.login(request, user)
            return redirect('.')

        else:             
             messages.info(request, uname + ', does not exist, Try to login again or Register!!!')
             return redirect('signin')
    else:
        return render(request,'signin.html')








