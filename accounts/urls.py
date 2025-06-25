from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
     path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('wishlist/add/<int:book_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('wishlist/', views.wishlist_view, name="wishlist")
]