from users_app.models import Users
from django.shortcuts import redirect, render, HttpResponse

def index(request):
    # context = request.session['xx']
    context = {
        "data": Users.objects.all()
    }
    return render(request, 'model.html', context)

def add(request):
    Users.objects.create(first_name= request.POST['fname'], last_name= request.POST['lastname'], email_adress= request.POST['email'], age= request.POST['age'])
    # request.session['xx'] = {
    #     "data": Users.objects.all()
    # }
    # request.session['aa'] = Users.objects.last()
    # request.session['bb'] = Users.objects.get(id=2)
    # request.session['cc'] = Users.objects.get(id=3)
    # request.session['dd'] = Users.objects.get(id=1)
    return redirect('/')

def delete(request):
    c = Users.objects.all()
    c.delete()
    return redirect('/')
