from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def group_page(request):
    context = {}
    return render(request, 'garage_services/group_page.html', context)
