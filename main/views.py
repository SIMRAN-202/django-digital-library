from django.shortcuts import render
from django.http import HttpResponse
from main.models import Book, Category, Testimonial
from django.db.models import Q
from accounts.models import Wishlist 


def home(req):
    featured_books = Book.objects.all()[:4]
    categories = Category.objects.all()
    testimonials = Testimonial.objects.all()
    return render(req, "home.html", {
        'featured_books':featured_books,
        'categories':categories,
        'testimonials':testimonials
        })


def about(req):
    return render(req, 'about.html')

def contact(req):
    return render(req, 'contact.html')


def library(req):
    books = Book.objects.all()
    categories = Category.objects.all()
    
    wishlist_book_ids = []
    if req.user.is_authenticated:
        wishlist_book_ids = Wishlist.objects.filter(user=req.user).values_list('book__id', flat=True)

    return render(req, 'library.html', {
        'categories': categories,
        'books': books,
        'wishlist_book_ids': wishlist_book_ids
    })


def library_by_category(req, category_id):
    categories = Category.objects.all()
    selected_category = Category.objects.get(id=category_id)
    books = Book.objects.filter(category=selected_category)
    return render(req, 'library.html', {
        'books': books,
        'selected_category': selected_category,
        'categories':categories
    })

def search_books(req):
    query = req.GET.get('q')
    books = []
    if query:
        books = Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query) | Q(description__icontains=query) )
    return render(req, 'search_results.html',{
        'books':books,
        'query':query
    })

def book_details(req, book_id):
    book = Book.objects.get(id=book_id)
    related_books = Book.objects.filter(category=book.category).exclude(id=book_id)[:4]

    in_wishlist = False

    if req.user.is_authenticated:
        in_wishlist = Wishlist.objects.filter(user=req.user, book=book).exists()

    return render(req, 'book_details.html',{
        'book':book,
        'related_books':related_books,
        'in_wishlist':in_wishlist
    })