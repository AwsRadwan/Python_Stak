from django.shortcuts import render, HttpResponse, redirect
def form(request):
    return render(request, 'formd.html')

def result(request, method=['POST']):
    request.session['yname'] = request.POST['yo_na']
    request.session['loc'] = request.POST['location']
    request.session['fav'] = request.POST['fl']
    request.session['com'] = request.POST['comment']
    request.session['gg'] = request.POST['gender']
    # cont = {
    #     'yname': yname,
    #     'loc': loc,
    #     'fav': fav,
    #     'com': com,
    #     'gg': gg
    # }
    return redirect("/success")

def success(request):
    return render(request,"resultd.html")