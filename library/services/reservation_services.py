from django.shortcuts import render, redirect
from library.forms import ReservationBookForm
from library.models import Book, Category, ReservationBook


def view(request, id):
    data = {
        'book': Book.objects.get(id=id),
        'category': Category.objects.all(),
        'form': ReservationBookForm()
    }
    return render(request, 'book/book_view.html', data)


def reserve(request):
    if request.method == 'POST':
        form = ReservationBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reserve.list')
    else:
        form = ReservationBookForm()
        return render(request, 'book/book_reserve.html', {'form': form})


def list(request):
    data = {
        'category': Category.objects.all(),
        'reserves': ReservationBook.objects.all()
    }
    return render(request, 'reserve/reserve.list.html', data)
