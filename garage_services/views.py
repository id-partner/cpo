from django.shortcuts import render
from django.http import HttpResponse


def index_handler(request):
    context = {}
    return render(request, 'garage_services/group_page.html', context)

def brand_handler(request):
    context = {}
    return render(request, 'garage_services/brand_page.html', context)

def robots_handler(request):
    return render (request,'garage_services/robots.txt', content_type='text/plain')
