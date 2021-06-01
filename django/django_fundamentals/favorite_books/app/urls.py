from django.urls import path     
from . import views
urlpatterns = [
    path('', views.main),
    path('log_reg', views.login_register),
    path('logout', views.log_out),
    path('books', views.books),
    path('books/add_book', views.add_book),
    path('books/show/<int:id>', views.show_this),
    path('add_fav/<int:id>', views.add_fav),
    path('update/<int:id>', views.update),
    path('remove/<int:id>', views.remove),
    path('delete/<int:id>', views.delete),
    ]
