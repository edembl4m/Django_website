from django.shortcuts import render
from django.views.generic import View, DetailView, ListView
from django.views.generic.base import View

from .models import Category, Moped, Scooter, QuadBike, PitBike, CrossTechnique, Category, Gallery
from .mixins import CategoryDetailMixin

from django.core.paginator import Paginator


class MainView(View):

    def get(self, request, *args, **kwargs):
        categories = Category.objects.get_categories_for_nav()
        return render(request, 'index.html', {'categories': categories})


# def index(request):
#     categories = Category.objects.get_categories_for_nav()
#     return render(request, 'index.html', {'categories': categories})


class ProductDetailView(CategoryDetailMixin, DetailView):

    CT_MODEL_MODEL_CLASS = {
        'mopeds': Moped,
        'scooters': Scooter,
        'quadbikes': QuadBike,
        'pitbikes': PitBike,
        'crosstechiniques': CrossTechnique,
    }

    def dispatch(self, request, *args, **kwargs):
        self.model = self.CT_MODEL_MODEL_CLASS[kwargs['ct_model']]
        self.queryset = self.model._base_manager.all()
        return super().dispatch(request, *args, **kwargs)
    
    # model= Model
    # queryset = Model.object.all()
    context_object_name = 'product'
    template_name = 'product_detail.html'
    sluq_url_kwarg = 'slug'
    # paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ct_model'] = self.model._meta.model_name
        return context


# class ProductGallery(View):
#     model = Gallery
#     queryset = 


class CategoryDetailView(CategoryDetailMixin, DetailView, ListView):

    model = Category
    # queryset = Category.objects.all()
    object_list = Category.objects.filter()
    context_object_name = 'category'
    template_name = 'category_detail.html'
    slug_url_kwarg = 'slug'
    
    paginate_by = 2

