from django.shortcuts import render
from django.http import HttpResponse
from main.models import Book, Category, Testimonial


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
    return render(req, 'library.html')