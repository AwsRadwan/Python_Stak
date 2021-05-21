from django.http import request
from django.shortcuts import redirect, render, HttpResponse

def index(request):
    if 'count' in request.session:
        request.session['count'] += 1
    else:
        request.session['count'] = 1
    return render(request, 'counter.html')

def clear(request):
    request.session['count'] = 0
    return redirect('/')

def addtow(request):
    request.session['count'] += 1
    return redirect('/')

def add_num(request):
    request.session['count'] += int(request.POST['numv'])-1
    return redirect('/')