
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('library/', views.library, name="library"),
    path('library/category/<int:category_id>/' , views.library_by_category, name="library_by_category"),
    path('search/', views.search_books, name="search_books"),
    path('book/<int:book_id>/', views.book_details, name="book_details"),
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)