from django.shortcuts import render, redirect
def index(request):
    return render(request,"index.html")

def create_user(request, method = ['POST']):
    context = {
        "name_on_template" : request.session['namex'],
        "email_on_template" : request.session['emailx']
    }
    request.session['namex'] = request.POST['name']
    request.session['emailx'] = request.POST['email']
    return redirect("/success")

def success(request, method = ['POST']):
    # this is the success route
    return render(request,"success.html", request.session['namex'], request.session['emailx'])