from django.urls import path
from . import views

urlpatterns = [
    path('',       views.homepage, name='homepage'),
    path('about/', views.about,    name='about'),
    path('articles/',views.article_list, name='article_list'),
]
