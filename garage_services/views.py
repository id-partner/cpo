from django.shortcuts import render
from django.http import HttpResponse
from .models import Group
from company_info.models import Gallery, Partner


def index_handler(request):
    # vag = Group.objects(filter='Vag')
    gallery = Gallery.objects.all()
    partners = Partner.objects.all()
    context = {
        'name_en': 'VAG',
        'name_ru': 'ВАГ',
        'services': 'Услуги',
        'brands': 'Бренды',
        'reviews': 'отзывы',
        'gallery': gallery,
        'partners': partners,

    }
    return render(request, 'garage_services/group_page.html', context)


def brand_handler(request):
    context = {}
    return render(request, 'garage_services/brand_page.html', context)

def robots_handler(request):
    return render (request,'garage_services/robots.txt', content_type='text/plain')
