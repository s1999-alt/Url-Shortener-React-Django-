from django.urls import path
from . import views 

urlpatterns = [
    path('shortener/', views.link_shortener, name='shortener'),
    path('get-links/', views.get_links, name='get-links'),
    path('get-link/<str:hash>/', views.get_link, name='get-link'),
    path('delete-link/<str:hash>/', views.delete_link, name='delete-link'),
]