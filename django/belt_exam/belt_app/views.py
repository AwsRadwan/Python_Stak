from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import *
import bcrypt


def main(request):
    return render(request, 'log_in.html')

def login_register(request):
    if 'register' in request.POST:
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        errors = User.objects.register(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
            new_user = User.objects.create(first_name = fname, last_name = lname, email = email, password = pw_hash)
            request.session['id'] = new_user.id
            request.session['fname'] = fname
            request.session['lname'] = lname
            return redirect('/thoughts')

    if 'login' in request.POST:
        errors2 = User.objects.login(request.POST)
        if len(errors2) > 0:
            for key, value in errors2.items():
                messages.error(request, value)
            return redirect('/')
        email = request.POST['emaill']
        password = request.POST['passwordd']
        x = User.objects.filter(email = email)
        user=x.first()
        if x:
            if bcrypt.checkpw(request.POST['passwordd'].encode(), user.password.encode()):
                request.session['id'] = user.id
                request.session['fname'] = user.first_name
                request.session['lname'] = user.last_name
                return redirect('/thoughts')
            return redirect('/')
        return redirect('/')
    return redirect('/')

def log_out(request):
    del request.session['id']
    del request.session['fname']
    del request.session['lname']
    return redirect('/')

def thoughts(request):
    if 'id' in request.session:
        data = {
            'posts': Post.objects.all(),
            'users': User.objects.all(),
            'user': User.objects.get(id = request.session['id'])
        }
        return render(request, 'thoughts.html', data)
    return redirect('/')

def add_post(request):
    errors3 = User.objects.post(request.POST)
    if len(errors3) > 0:
        for key, value in errors3.items():
            messages.error(request, value)
        return redirect('/thoughts')
    user = User.objects.get(id = request.session['id'])
    new_post = Post.objects.create(post = request.POST['add_post'], user = user)
    new_post.users_liked.add(user)
    return redirect('/thoughts')

def delete(request, id):
    post = Post.objects.get(id = id)
    post.delete()
    return redirect('/thoughts')

def post_details(request, id):
    if 'id' in request.session:
        data = {
            'posts': Post.objects.all(),
            'users': User.objects.all(),
            'user': User.objects.get(id = request.session['id']),
            'post': Post.objects.get(id = id),
        }
        return render(request, 'post_details.html', data)
    return redirect('/')

def like(request, id):
    user = User.objects.get(id = request.session['id'])
    post = Post.objects.get(id = id)
    user.liked_posts.add(post)
    return redirect('/thoughts/'+str(id))


def dislike(request, id):
    user = User.objects.get(id = request.session['id'])
    post = Post.objects.get(id = id)
    user.liked_posts.remove(post)
    return redirect('/thoughts/'+str(id))