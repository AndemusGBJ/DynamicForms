
from django.contrib import admin
from django.urls import path

from books.views import (
    creat_book,
    create_book_form,
    detail_book,
    update_book,
    delete_book)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('htmx/book-form', create_book_form, name = "book-form"),
    path('htmx/book-form/<pk>/', detail_book, name = "detail-book"),
    path('htmx/book-form/<pk>/update', update_book, name = "update-book"),
    path('htmx/book-form/<pk>/delete', delete_book, name = "delete-book"),
    path('<pk>/', creat_book, name="create-book"),

]
