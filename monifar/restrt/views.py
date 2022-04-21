from pickletools import anyobject
from subprocess import PIPE
from django.shortcuts import render
from django.http import HttpResponse
from .models import intel

# Create your views here.
def index(request):

      i = intel()
      i.id = 1
      i.ids = '0' + str(i.id)
      i.name = 'Tasty'
      i.details = 'Our food is delicious!!!'
      i.st = True

      j = intel()
      j.id = 2
      j.ids = '0' + str(j.id)
      j.name = 'Yummy'
      j.details = 'Our food is Creamy!!!'
      j.st = True

      k = intel()
      k.id = 3
      k.ids = '0' + str(k.id)
      k.name = 'Spicy'
      k.details = 'Our food is Pepperish!!!'
      k.st = False

      l = intel()
      l.food = 'Commodores Resturant'

      m = intel()
      m.det = 'welcome to Commodores Resturant'
      m.intro = 'We serve the best food'

      c = intel()
      c.call_centre = '08091659364'
      c.time = 'mon - sat :9am-6pm'
      c.address = 'No 1 ogbe cresent,pipeline,ilorin,kwara-state'
      c.email = 'commodores@gmail.com'
      c.start = 'lobster and crabs'
      c.filst = ".filter-c.start"
      





      features = [i,j,k,l,m,c]
      

      context={
            'features':features
            

      }
      return render(request,'index.html',context)


