from pickletools import anyobject
from subprocess import PIPE
from django.shortcuts import render
from django.http import HttpResponse
from .models import intel

# Create your views here.
def index(request):
    name = 'ayo'
    age = '21'

    context = (
          'name':name,
          'age':age,
    )      
          
    return render(request,'index.html', context)
