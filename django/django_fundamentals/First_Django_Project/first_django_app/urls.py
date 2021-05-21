from django.urls import path
from . import views
urlpatterns = [
    path('/', views.root),
    path('/blogs', view.index),
    path('/blogs/new', view.new),
    path('/blogs/creat', view.creat),
    path('/blogs/<number>', view.show),
    path('/blogs/<number>/edit', view.edit),
    path('/blogs/<number>/delete', view.destroy),
]