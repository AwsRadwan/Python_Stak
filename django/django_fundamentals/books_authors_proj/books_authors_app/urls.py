from django.urls import path     
from . import views

urlpatterns = [
    path('', views.author_page),
    path('author', views.add_author),
    path('author/<int:num>', views.author_data),
    path('author/<int:num>/add_book_to_author', views.a_book),
    path('gobook', views.book_page),
    path('book', views.add_book),
    path('book/<int:num>', views.book_data),
    path('book/<int:num>/add_author_to_book', views.a_author),
    ]