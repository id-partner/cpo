from django.urls import path

from . import views

urlpatterns = [
    path('', views.newslist_handler),
    path('news/', views.news_handler),
]


