from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from library.models import Book
from library.services import (
    category_services,
    book_services,
    user_services,
    reservation_services
)


def page_home(resquest):
    books = Book.objects.all()
    data = {'books': books}
    return render(resquest, 'index.html', data)


def page_book(resquest):
    return render(resquest, 'livros_lista.html')


# Category
def category_list(request):
    data = category_services.list(request)
    return data


@login_required
def category_create(request):
    data = category_services.create(request)
    return data


@login_required
def category_update(request, id):
    data = category_services.update(request, id)
    return data


@login_required
def category_delete(request, id):
    data = category_services.delete(request, id)
    return data


# book
def book_list(request):
    data = book_services.list(request)
    return data


@login_required
def book_create(request):
    data = book_services.create(request)
    return data


@login_required
def book_update(request, id):
    data = book_services.update(request, id)
    return data


@login_required
def book_delete(request, id):
    data = book_services.delete(request, id)
    return data


def signup(request):
    data = user_services.signup(request)
    return data


def profile(resquest):
    return render(resquest, 'student/profile.html')


# Reservation
def book_view(request, id):
    data = reservation_services.view(request, id)
    return data


def book_reserve(request):
    data = reservation_services.reserve(request)
    return data


# Reservation list

def reserve_list(request):
    data = reservation_services.list(request)
    return data
