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
        c = 'The area of a rectangle ' + str(l*w) +'cm^2'
        context = {
            'res':c 
    
            }
            
        return render(request, 'geometric.html', context)


def geometric(request):

    l = request.POST['length']
    w = request.POST['width']

    if l == '' or w == '':
        context = {'res':'No Data Entered!!!'}
        return render(request, 'geometric.html', context)  

    else:
        l = float(l)
        w = float(w)       
        d = 'The perimeter of a rectangle' + str(2*l + 2*w) + 'cm^2'
        context = {
            'res':d
    
            }
            
        return render(request, 'geometric.html', context)


def geometric(request):

    l = request.POST['length']
    
    if l == '' :
        context = {'res':'No Data Entered!!!'}
        return render(request, 'geometric.html', context)  

    else:
        l = float(l)       
        d = 'The length of a square' + str(l * l) + 'cm^2'
        context = {
            'res':d
    
            }
            
        return render(request, 'geometric.html', context)

def geometric(request):

    l = request.POST['length']
    
    if l == '' :
        context = {'res':'No Data Entered!!!'}
        return render(request, 'geometric.html', context)  

    else:
        l = float(l)       
        d = 'The length of a square' + str(4 * l) + 'cm^2'
        context = {
            'res':d
    
            }
            
        return render(request, 'geometric.html', context)









