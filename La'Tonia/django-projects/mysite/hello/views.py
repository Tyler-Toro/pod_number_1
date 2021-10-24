from django.http import request
from django.shortcuts import render

# Create your views here.
def hello(request):
    if request.method == 'GET':
        return render(request=request, template_name='hello.html')

def hello_name(request, name):
    if request.method == 'GET':
        return render(request=request, template_name='hello_name.html', context={ 'name': name })

def goodbye(request, name='Django'):
    if request.method == 'GET':
        # return render(request=request, template_name='goodbye.html', context={'name': name})
        return render( request=request, template_name='goodbye.html', context={'name': name })
        
def you_there(request, name):
    if request.method == 'GET':
        return render(request=request, template_name='you_there.html', context={'name': name})

def stay(request, name):
    if request.method == 'GET':
        return render(request=request, template_name='stay.html', context={'name': name})