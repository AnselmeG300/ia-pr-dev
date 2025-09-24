from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Category, Service


class CategoryListView(ListView):
    """View for listing all categories with their services."""
    model = Category
    template_name = 'categories_services/category_list.html'
    context_object_name = 'categories'

    def get_queryset(self):
        return Category.objects.prefetch_related('services').all()


class CategoryDetailView(DetailView):
    """View for displaying a single category and its services."""
    model = Category
    template_name = 'categories_services/category_detail.html'
    context_object_name = 'category'

    def get_queryset(self):
        return Category.objects.prefetch_related('services')


class ServiceDetailView(DetailView):
    """View for displaying a single service."""
    model = Service
    template_name = 'categories_services/service_detail.html'
    context_object_name = 'service'

    def get_queryset(self):
        return Service.objects.select_related('category')


def home_view(request):
    """Homepage view showing categories and services grouped together."""
    categories = Category.objects.prefetch_related('services').all()
    return render(request, 'categories_services/home.html', {'categories': categories})
