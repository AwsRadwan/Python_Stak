from books_authors_app.models import Author, Book
from django.shortcuts import render, HttpResponse, redirect
def author_page(request):
    # request.session['authors'] = Author.objects.all()
    context = {
        'author': Author.objects.all(),
        'book': Book.objects.all()
    }
    return render(request, 'add_author.html', context)

def add_author(request):
    Author.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], notes = request.POST['notes'])
    return redirect('/')

def author_data(request,num):
    context = {
        'author': Author.objects.get(id = num),
        'book': Book.objects.all(),
    }
    request.session['num'] = num
    return render(request, 'author_data.html', context)

def a_book(request, num):
    c = Author.objects.get(id = num)
    c.books.add(Book.objects.get(title = request.POST['select']))
    return redirect('/author/'+str(num))

################################################################################################################################

def book_page(request):
    context = {
        'author': Author.objects.all(),
        'book': Book.objects.all()
    }
    return render(request, 'add_book.html', context)

def add_book(request):
    Book.objects.create(title = request.POST['title'], desc = request.POST['desc'])
    return redirect('/gobook')

def book_data(request,num):
    context = {
        'author': Author.objects.all(),
        'book': Book.objects.get(id = num),
    }
    request.session['num'] = num
    return render(request, 'book_data.html', context)

def a_author(request, num):
    s = Book.objects.get(id = num)
    s.author.add(Author.objects.get(first_name = request.POST['select2']))
    return redirect('/book/'+str(num))