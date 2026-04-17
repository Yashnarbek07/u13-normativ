from http.client import HTTPResponse

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Books

# Create your views here.


def book_views(request):
    books = Books.objects.all()

    context = {
        "books" : books
    }

    return render(request, "books/book_list.html", context)


def book_detail_view(request, id):
    book = get_object_or_404(
        Books, id=id
    )

    context = {
        "book" : book
    }

    return render(request, "books/book_detail.html", context)


def create_book(request):
    return HttpResponse("Book has been created.")