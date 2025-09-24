from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('categories/', views.CategoryListView.as_view(), name='category-list'),
    path('categories/<int:pk>/', views.CategoryDetailView.as_view(), name='category-detail'),
    path('services/<int:pk>/', views.ServiceDetailView.as_view(), name='service-detail'),
]