from .views import book_views, book_detail_view
from django.urls import path
from . import views

urlpatterns = [
    path("books/book_list/", book_views, name="book_list"),
    path("books/book_detail/<int:id>/", book_detail_view, name="book_detail"),
    path("create/", views.create_book, name="create_book"),
]