from django.views.generic.detail import SingleObjectMixin
# from django.views.generic import ListView
from .models import Category, Moped, Scooter, QuadBike, PitBike, CrossTechnique
from django.core.paginator import Paginator

class CategoryDetailMixin(SingleObjectMixin):

    CATEGORY_SLUG2PRODUCT_MODEL = {
        'mopeds': Moped,
        'scooters': Scooter,
        'quadbikes': QuadBike,
        'pitbikes': PitBike,
        'crosstechiniques': CrossTechnique
    }

    def get_context_data(self, **kwargs):
        if isinstance(self.get_object(), Category):
            model = self.CATEGORY_SLUG2PRODUCT_MODEL[self.get_object().slug]
            context = super().get_context_data(**kwargs)
            context['categories'] = Category.objects.get_categories_for_nav()
            context['category_products'] = model.objects.all()
            # paginator = Paginator(context['category_products'], 2)
            return context
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.get_categories_for_nav()
        return context