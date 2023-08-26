from django.urls import path

# from .views import MainView, ProductDetailView
from . import views

urlpatterns = [
    path('', views.MainView.as_view(), name = 'index'),
    path('product/<str:ct_model>/<str:slug>', views.ProductDetailView.as_view(), name = 'product_detail'),
    path('category/<str:slug>', views.CategoryDetailView.as_view(), name = 'category_detail')
]