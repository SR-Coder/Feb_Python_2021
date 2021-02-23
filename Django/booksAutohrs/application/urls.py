from django.urls import path
from . import views

urlpatterns = [
    #Display 
    path('', views.index),
    path('authors', views.dispAuthors),
    path('books/<int:book_id>', views.dispBookDetail),



    #Action
    path('addBook', views.addNewBook),
    path('addAuthor', views.addNewAuthor),
    path('addAuthorToBook', views.addAuthorToBook),
]