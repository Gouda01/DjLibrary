from django.shortcuts import render
from .models import Book

# Create your views here.

from django.views.generic import ListView , DetailView ,UpdateView , CreateView , DeleteView

class BookList (ListView) :
    model = Book

class BookDetail (DetailView):
    model = Book

class AddBook (CreateView):
    model = Book
    fields = '__all__'
    success_url = '/books/'

class EditBook (UpdateView):
    model = Book
    fields = '__all__'
    success_url = '/books/'
    template_name = 'books/edit.html'

class DeleteBook (DeleteView) :
    model = Book
    success_url = '/books/'

