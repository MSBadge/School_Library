from django.shortcuts import render
from books.models import Book
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView


class BooksList(ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'books'

class AddBook(CreateView):
    model = Book
    template_name = 'books/add_book.html'
    fields = ['title', 'author', 'description', 'genre', 'isbn', 'publication_date']
    success_url = '/'

class BookDetail(DetailView):
    model = Book
    template_name = 'books/book_detail.html'
    context_object_name = 'book'


class EditBook(UpdateView):
    model = Book
    template_name = 'books/book_form.html'
    fields = ['title', 'author', 'description', 'genre', 'isbn', 'publication_date']
    success_url = '/'


class DeleteBook(DeleteView):
    model = Book
    template_name = 'books/book_confirm_delete.html'
    success_url = '/'