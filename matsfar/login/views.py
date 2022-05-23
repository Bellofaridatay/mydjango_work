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
        first = request.POST['first']
        other = request.POST['other']
        last = request.POST['last']
        faculty = request.POST['faculty']
        gender = request.POST['gender']
        level = request.POST['level']

        if pword == cpword:

            if User.objects.filter(username=uname).exists():
                messages.info(request, uname + ', already exist, Try another Username!!!')
                return redirect('register')

            elif User.objects.filter(email=email).exists():
                messages.info(request, email + ', already exist, Try another Email Address!!!')
                return redirect('register')

            else:
                user = User.objects.create_user(username=uname, email=email, password=pword)
                lg = detail.objects.create(uname=uname, dept=dept, first=first, other=other, last=last, faculty=faculty, gender=gender,level=level)
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
            dt = detail.objects.get(uname=uname)
            return render(request,'index.html',{'dt':dt})

        else:
            messages.info(request, 'Invalid Login Details!!!')
            return redirect('signin')


    else:
        return render(request,'signin.html')


def settings(request):

    return render(request,'settings.html')   


def logout(request):
    auth.logout(request)
    return redirect('.')

    return render(request,'index.html') 


def delete(request):
    auth.delete(request)
    return redirect('.')

    return render(request,'index.html') 
            
        


def change(request):   
 if request.method == 'POST':

       Name = request.POST[' Name']
       email = request.POST[' email']
       dept = request.POST[' dept']
       
       if Name == Name:

              if User.objects.filter(Name=Name):
                     messages.info(request, Name + ' , succesfully changed!!!')
                     return redirect('settings')

              elif User.objects.filter(email=email, dept=dept):
                    messages.info(request, + ', succesfully changed!!!')
                    return redirect('settings')

              else:
                  user = User.objects.create_user(Name=Name, email=email,dept=dept)
                  user.save()
                  return redirect('settings')

       else:
            return redirect('settings')
 else:
    return render(request,'change.html')   



def cpw(request):

    if request.method == 'POST':

        pword = request.POST['pword']
        cpword = request.POST['cpword']
        

        if pword == cpword:

             messages.info(request, cpword + ', has been changed successfully!!!')
             return redirect('change')

            
        else:
            messages.info(request, 'Password does not match!!!')

            return redirect('cpwd')
    else:
        return render(request,'cpwd.html')         

        





