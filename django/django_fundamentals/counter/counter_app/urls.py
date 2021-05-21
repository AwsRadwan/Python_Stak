from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('clear', views.clear),
    path('add2', views.addtow),
    path('addnumxx', views.add_num),
]