from django.db.models import Avg, Max
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Book
# Create your views here.
def index(request):
    books = Book.objects.all().order_by('')
    num_books = books.count()
    avg_rating = books.aggregate(Avg('rating'))
    return render(request, 'book_outlet/index.html', {
        'books': books,
        "total_number_of_books": num_books,
        "average_rating": avg_rating,
    })

def book_detail(request, slug):

    # try:
    #     book = Book.objects.get(pk=book_id)
    #     return render(request, 'book_outlet/book_detail.html', {
    #         'title': book.title,
    #         'author': book.author,
    #         'rating':book.rating,
    #         'is_bestselling': book.is_bestselling,
    #     })
    # except:
    #     raise Http404('Book not found')

    book = get_object_or_404(Book, slug=slug)
    return render(request, 'book_outlet/book_detail.html', {
        'title': book.title,
        'author': book.author,
        'rating':book.rating,
        'is_bestselling': book.is_bestselling,
    })

