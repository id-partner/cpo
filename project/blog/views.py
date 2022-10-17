from django.shortcuts import render
from django.http import HttpResponse

def newslist_handler(request):
    context = {}
    return render(request, 'blog/news_list.html', context)

def news_handler(request):
    context = {}
    return render(request, 'blog/news_page.html', context)

