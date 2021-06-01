from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import *
import bcrypt

def main(request):
    return render(request, 'login.html')

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
            return redirect('/books')
    if 'login' in request.POST:
        email = request.POST['emaill']
        password = request.POST['passwordd']
        x = User.objects.filter(email = email)
        user=x.first()
        if x:
            if bcrypt.checkpw(request.POST['passwordd'].encode(), user.password.encode()):
                request.session['id'] = user.id
                request.session['fname'] = user.first_name
                request.session['lname'] = user.last_name
                return redirect('/books')
            return redirect('/')
        return redirect('/')
    return redirect('/')

def log_out(request):
    del request.session['id']
    del request.session['fname']
    del request.session['lname']
    return redirect('/')

def books(request):
    if 'id' in request.session:
        all_books = {
            'books': Book.objects.all(),
            'users': User.objects.all(),
            'user': User.objects.get(id = request.session['id'])
        }
        return render(request, 'books.html', all_books)
    return redirect('/')

def add_book(request):
    user = User.objects.get(id = request.session['id'])
    new_book = Book.objects.create(title = request.POST['title'], desc = request.POST['desc'], uploaded_by = user)
    new_book.users_liked.add(user)
    return redirect('/books')

def add_fav(request, id):
    user = User.objects.get(id = request.session['id'])
    book = Book.objects.get(id = id)
    book.users_liked.add(user)
    return redirect('/books')

def show_this(request, id):
    data = {
        'book': Book.objects.get(id =id),
        'user': User.objects.get(id = request.session['id']),
        'books': Book.objects.all(),
        'users': User.objects.all(),
    }
    return render(request, 'this_book.html', data)

def remove(request, id):
    user = User.objects.get(id = request.session['id'])
    book = Book.objects.get(id = id)
    user.liked_books.remove(book)
    return redirect('/books')

def update(request, id):
    user = User.objects.get(id = request.session['id'])
    book = Book.objects.get(id = id)
    book.desc = request.POST['des']
    book.save()
    return redirect('/books')

def delete(request, id):
    book = Book.objects.get(id = id)
    book.delete()
    return redirect('/books')