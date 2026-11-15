from django.shortcuts import render, redirect
from myapp.models import Book
from myapp.my_forms import BookForm

def show_books(request):
    books = Book.objects.all()
    return render(request, 'show_books.html', {'books': books})

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_books')
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})
#Book.objects.create(title='River and the source',year=2021,category='Fiction',cost=450,isbn='2342242',published=True)
    #Book.objects.create(title='Henry the coder', year=2025, category='Fiction', cost=450, isbn='2342632',
                       # published=True)
def delete_book(request,id):
    book = Book.objects.get(id=id) # select * from book where id = 34
    book.delete()
    return redirect('show_books')


def edit_book(request,id):
    return render(request, 'edit_book.html', {'book': Book.objects.get(id=id)})