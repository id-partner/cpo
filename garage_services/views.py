from django.shortcuts import render
from django.http import HttpResponse
from .models import CarModel, Group, Service, Brand, ImageDesing
from django.views.generic import ListView, TemplateView, DetailView
from company_info.models import Gallery, Partner, Worker, Review, SourceReview


# def index_handler(request):
#     # vag = Group.objects(filter='Vag')
#     gallery = Gallery.objects.all()
#     partners = Partner.objects.all()
#     context = {
#         'name_en': 'VAG',
#         'name_ru': 'ВАГ',
#         'services': 'Услуги',
#         'brands': 'Бренды',
#         'reviews': 'отзывы',
#         'gallery': gallery,
#         'partners': partners,

#     }
#     return render(request, 'garage_services/group_page.html', context)


def brand_handler(request):
    context = {}
    return render(request, 'garage_services/brand_page.html', context)


class RobotsView(TemplateView):
    template_name = 'garage_services/robots.txt'
    content_type = 'text/plain'


class IndexView(ListView):
    model = Group
    template_name = 'garage_services/index_list.html'
    context_object_name = 'groups'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = Service.objects.prefetch_related('child_category').filter(order='1')
        context['gallery'] = Gallery.objects.all()
        context['partners'] = Partner.objects.all()
        context['workers'] = Worker.objects.all()
        context['sources'] = SourceReview.objects.all()
        return context

class GroupView(DetailView):
    'страница бренда'
    model = Group
    template_name = 'garage_services/group_detail.html'
    context_object_name = 'group'
    slug_url_kwarg = 'group_slug'
    allow_empty = False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['brands'] = Brand.objects.filter(group__slug=self.kwargs.get('group_slug'))
        context['services'] = Service.objects.all()
        context['gallery'] = Gallery.objects.all()
        context['partners'] = Partner.objects.all()
        context['workers'] = Worker.objects.all()
        context['sources'] = SourceReview.objects.all()
        return context


class BrandView(DetailView):
    '''
    страница марки
    добавить заголовок к маркам в шаблоне
    '''
    
    model = Brand
    template_name = 'garage_services/brand_detail.html'
    context_object_name = 'brand'
    slug_url_kwarg = 'brand_slug'
    allow_empty = False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # разобраться с передачей слага и сокращением числа запросов
        imagedesing = ImageDesing.objects.filter(brand__slug=self.get_object().slug)
        # в шаблоне сделать защиту от дурака
        if imagedesing:
            context['logo_bg'] = imagedesing.get(position ='LOGO_BG')
            context['first_bg'] = imagedesing.get(position ='FIRST')

        context['models']= CarModel.objects.filter(brand__slug=self.get_object().slug)
        context['services'] = Service.objects.all()
        context['gallery'] = Gallery.objects.all()
        context['partners'] = Partner.objects.all()
        context['workers'] = Worker.objects.all()
        context['sources'] = SourceReview.objects.all()

        return context


class ModelView(DetailView):
    '''
    страница модели
    добавить заголовок к маркам в шаблоне
    '''
    
    model = CarModel
    template_name = 'garage_services/model_detail.html'
    context_object_name = 'model'
    slug_url_kwarg = 'model_slug'
    allow_empty = False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # разобраться с передачей слага и сокращением числа запросов
        imagedesing = ImageDesing.objects.filter(carmodel__slug=self.get_object().slug)
        # в шаблоне сделать защиту от дурака
        if imagedesing:
            context['logo_bg'] = imagedesing.get(position ='LOGO_BG')
            context['first_bg'] = imagedesing.get(position ='FIRST')

        # context['models']= CarModel.objects.filter(brand__slug=self.get_object().slug)
        context['services'] = Service.objects.all()
        context['gallery'] = Gallery.objects.all()
        context['partners'] = Partner.objects.all()
        context['workers'] = Worker.objects.all()
        context['sources'] = SourceReview.objects.all()

        return context

# вьюха услуги без привязки к модели
# вьюха услуга с брендом/макрой/моделью/кузовом

