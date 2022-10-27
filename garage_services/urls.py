from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='home' ),
    path('robots.txt', views.RobotsView.as_view(), name='robots'),

    path('<group_slug>', views.GroupView.as_view(), name='group_detail'),
    path('<group_slug>/remont-<brand_slug>', views.BrandView.as_view(), name='brand_detail'),
]