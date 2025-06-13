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