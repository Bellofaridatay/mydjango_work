from subprocess import PIPE
from django.shortcuts import render
from django.http import HttpResponse
from .models import intel

# Create your views here.

def index(request):
    intel1 = intel()
    intel2 = intel()
    intel3 = intel()
    intel4 = intel()

    intel1.id = 1
    intel1.det = 'Your health is important to us'
    intel1.st = True

    intel2.id = 2
    intel2.det = 'Your life is precious to us'
    intel2.st = True

    intel3.id = 3
    intel3.det = 'You can never die in our clinic'
    intel3.st = False

    intel4.id = 4
    intel4.det = 'Outpatient Facility is Available'
    intel4.st = False


    context = {
        'intels' : [intel1,intel2,intel3,intel4],
}
    return render(request,'index.html', context)



def sum(request):

    a = request.POST['first']
    b = request.POST['second']

    if a == '' or b == '':
        context = {'res':'No Data Entered!!!'}
        return render(request, 'sum.html', context)  

    else:
        a = float(a)
        b = float(b)       
        c = 'The result is ' + str(a + b)
        context = {
            'res': c
            }
        return render(request, 'sum.html', context)



def rectangle(request):

    l = request.POST['length']
    w = request.POST['width']

    if l == '' or w == '':
        context = {'res':'No Data Entered!!!'}
        return render(request, 'rectangle.html', context)  

    else:
        l = float(l)
        w = float(w)       
        area = 'The area of the rectangle = ' + str(l*w) +'cm^2'
        peri = 'The perimeter of the rectangle = ' + str((2*l)+(2*w)) +'cm'
        context = {
            'area':area, 
            'peri':peri
    
            }
            
        return render(request, 'rectangle.html', context)


def square(request):

    l = request.POST['length']

    if l == '' :
        context = {'res':'No Data Entered!!!'}
        return render(request, 'square.html', context)  

    else:
        l = float(l)
      
        area = 'The area of the square = ' + str(l*l) +'cm^2'
        peri = 'The perimeter of the square = ' + str(4*l) +'cm'
        context = {
            'area':area, 
            'peri':peri
    
            }
            
        return render(request, 'square.html', context)  

def circle(request):

    p = request.POST['p']
    r = request.POST['radius']

    if p == '' or r == '':
        context = {'res':'No Data Entered!!!'}
        return render(request, 'circle.html', context)  

    else:
        p = float(p)
        r = float(r)       
        circumference = 'The circumference of the circle = ' + str(2*p*r) +'cm'
        area = 'The area of the circle = ' + str(p*r*r) +'cm^2'
        context = {
            'circumference':circumference, 
            'area':area
    
            }
            
        return render(request, 'circle.html', context)             







