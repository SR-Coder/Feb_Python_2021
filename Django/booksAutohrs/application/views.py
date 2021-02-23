from django.shortcuts import render, HttpResponse, redirect
from . models import Book, Author

# Create your views here.
def index(request):
    context = {
        'all_books': Book.objects.all()
    }
    return render(request, 'books.html', context)

def dispAuthors(request):
    context = {
        'all_authors': Author.objects.all()
    }
    return render(request, 'authors.html', context)

def dispBookDetail(request, book_id):
    context = {
        "book_detail": Book.objects.get(id=book_id),
        "all_authors": Author.objects.all()
    }
    return render(request,'bookDetail.html', context)




#Action Methods
def addNewBook(request):
    new_book = Book.objects.create(
        title = request.POST['title'],
        description = request.POST['description']
    )
    return redirect('/')

def addNewAuthor(request):
    new_author = Author.objects.create(
        first_name = request.POST['fName'],
        last_name = request.POST['lName'],
        notes = request.POST['notes']
    )
    return redirect('/authors')


def addAuthorToBook(request):
    # getting the variables from the POST dictionary
    book_id = int(request.POST['book_id'])  
    author_id = int(request.POST['author'])
    # retriving the objects from the database
    thisBook = Book.objects.get(id=book_id)
    thisAuthor = Author.objects.get(id=author_id)
    # this command connects the two via a Many 2 many field
    thisBook.authors.add(thisAuthor)

    return redirect(f'/books/{book_id}')