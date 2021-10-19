from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .models import Book, Author
from .forms import BookFormSet, BookForm


def creat_book(request, pk):
    author = Author.objects.get(pk=pk)
    books = Book.objects.filter(author=author)
    form = BookForm(request.POST or None)

    if request.method== 'POST':
        if form.is_valid():
            book = form.save(commit=False)
            book.author = author
            book.save()
            return redirect("detail-book", pk=book.id)
        else:
            return render(request,"partials/book_form.html", {"form":form})

    context = {
        "form":form,
        "author":author,
        "books": books,
    }
    return render(request,'create_book.html', context)


def create_book_form(request):

    context = {
        "form": BookForm()
    }
    return render(request, "partials/book_form.html", context)

def detail_book(request, pk):
    book = Book.objects.get(pk=pk)
    context = {
        "book": book
    }
    return render(request, "partials/book_detail.html", context)

def update_book(request, pk):
    book = Book.objects.get(pk=pk)
    form = BookForm(request.POST or None, instance=book)
    if request.method== 'POST':
        if form.is_valid():
            book.save()
            return redirect("detail-book", pk=book.id)

    context = {
        "form": form,
        "book": book
    }
    return render(request, "partials/book_form.html", context)

def delete_book(request, pk):
    book = Book.objects.get(pk=pk)
    book.delete()
    return HttpResponse('')