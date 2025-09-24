from django.contrib import admin
from .models import Category, Service


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Admin interface for Category model."""
    list_display = ['name', 'description', 'service_count', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name', 'description']
    readonly_fields = ['created_at', 'updated_at']

    def service_count(self, obj):
        return obj.services.count()
    service_count.short_description = 'Number of Services'


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    """Admin interface for Service model."""
    list_display = ['name', 'category', 'created_at']
    list_filter = ['category', 'created_at']
    search_fields = ['name', 'description', 'category__name']
    readonly_fields = ['created_at', 'updated_at']
    list_select_related = ['category']
