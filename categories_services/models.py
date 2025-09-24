from django.db import models
from django.urls import reverse


class Category(models.Model):
    """Model representing a service category."""
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, help_text="Optional description of the category")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category-detail', args=[str(self.id)])


class Service(models.Model):
    """Model representing a service within a category."""
    name = models.CharField(max_length=200)
    description = models.TextField(help_text="Description of the service")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='services')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        unique_together = ['name', 'category']

    def __str__(self):
        return f"{self.name} ({self.category.name})"

    def get_absolute_url(self):
        return reverse('service-detail', args=[str(self.id)])
