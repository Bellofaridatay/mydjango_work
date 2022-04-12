from subprocess import PIPE
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    name = 'ayo'
    age = 25
    email = 'ayo@gmail.com'

    context = {
            'name':name,
            'age':age,
            'email':email,
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



def geometric(request):

    l = request.POST['length']
    w = request.POST['width']

    if l == '' or w == '':
        context = {'res':'No Data Entered!!!'}
        return render(request, 'geometric.html', context)  

    else:
        l = float(l)
        w = float(w)       
        area = 'The area of the rectangle = ' + str(l*w) +'cm^2'
        peri = 'The perimeter of the rectangle = ' + str((2*l)+(2*w)) +'cm'
        context = {
            'area':area, 
            'peri':peri
    
            }
            
        return render(request, 'geometric.html', context)


def geometric(request):

    l = request.POST['length']

    if l == '' :
        context = {'res':'No Data Entered!!!'}
        return render(request, 'geometric.html', context)  

    else:
        l = float(l)
      
        area = 'The area of the square = ' + str(l*l) +'cm^2'
        peri = 'The perimeter of the square = ' + str(4*l) +'cm'
        context = {
            'area':area, 
            'peri':peri
    
            }
            
        return render(request, 'geometric.html', context)  

def geometric(request):

    p = request.POST['p']
    r = request.POST['radius']

    if p == '' or r == '':
        context = {'res':'No Data Entered!!!'}
        return render(request, 'geometric.html', context)  

    else:
        p = float(p)
        r = float(r)       
        circumference = 'The circumference of the circle = ' + str(2*p*r) +'cm'
        area = 'The area of the circle = ' + str(p*r*r) +'cm^2'
        context = {
            'circumference':circumference, 
            'area':area
    
            }
            
        return render(request, 'geometric.html', context)             







