from django.urls import path

from . import views

urlpatterns = [
    path('', views.newslist_handler, name='blog'),
    path('news/', views.news_handler, name='single_news'),
]


