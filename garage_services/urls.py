from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='home' ),
    path('robots.txt', views.RobotsView.as_view(), name='robots'),

    path('avtoservis-<group_slug>', views.GroupView.as_view(), name='group_detail'),
    path('remont-<brand_slug>-v-ekaterinburge', views.BrandView.as_view(), name='brand_detail'),
    path('remont-<brand_slug>-<model_slug>', views.ModelView.as_view(), name='model_detail'),
]