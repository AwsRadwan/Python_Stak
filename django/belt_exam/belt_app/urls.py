from django.urls import path     
from . import views
urlpatterns = [
    path('', views.main),
    path('log_reg', views.login_register),
    path('log_out', views.log_out),
    path('thoughts', views.thoughts),
    path('add_post', views.add_post),
    path('delete_p/<int:id>', views.delete),
    path('thoughts/<int:id>', views.post_details),
    path('like/<int:id>', views.like),
    path('dislike/<int:id>', views.dislike),
    ]