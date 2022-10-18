from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_handler),
    path('skoda/', views.brand_handler),
    path('robots.txt', views.robots_handler),
]