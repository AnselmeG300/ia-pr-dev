from django.shortcuts import render, get_object_or_404
from .models import Category, Service


def category_list(request):
    """Display all categories with their services."""
    categories = Category.objects.prefetch_related('services').all()
    return render(request, 'services/category_list.html', {'categories': categories})


def category_detail(request, category_id):
    """Display services for a specific category."""
    category = get_object_or_404(Category, id=category_id)
    services = category.services.filter(is_active=True)
    return render(request, 'services/category_detail.html', {
        'category': category,
        'services': services
    })
