from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Category, Service


class CategoryModelTest(TestCase):
    """Test cases for Category model."""

    def setUp(self):
        self.category = Category.objects.create(
            name="Test Category",
            description="A test category description"
        )

    def test_category_creation(self):
        """Test that a category is created correctly."""
        self.assertEqual(self.category.name, "Test Category")
        self.assertEqual(self.category.description, "A test category description")
        self.assertTrue(self.category.created_at)
        self.assertTrue(self.category.updated_at)

    def test_category_str_method(self):
        """Test the string representation of Category."""
        self.assertEqual(str(self.category), "Test Category")

    def test_category_get_absolute_url(self):
        """Test the get_absolute_url method."""
        expected_url = reverse('category-detail', args=[self.category.id])
        self.assertEqual(self.category.get_absolute_url(), expected_url)


class ServiceModelTest(TestCase):
    """Test cases for Service model."""

    def setUp(self):
        self.category = Category.objects.create(
            name="Test Category",
            description="A test category"
        )
        self.service = Service.objects.create(
            name="Test Service",
            description="A test service description",
            category=self.category
        )

    def test_service_creation(self):
        """Test that a service is created correctly."""
        self.assertEqual(self.service.name, "Test Service")
        self.assertEqual(self.service.description, "A test service description")
        self.assertEqual(self.service.category, self.category)
        self.assertTrue(self.service.created_at)
        self.assertTrue(self.service.updated_at)

    def test_service_str_method(self):
        """Test the string representation of Service."""
        expected_str = f"Test Service (Test Category)"
        self.assertEqual(str(self.service), expected_str)

    def test_service_get_absolute_url(self):
        """Test the get_absolute_url method."""
        expected_url = reverse('service-detail', args=[self.service.id])
        self.assertEqual(self.service.get_absolute_url(), expected_url)


class ViewsTest(TestCase):
    """Test cases for views."""

    def setUp(self):
        self.client = Client()
        self.category = Category.objects.create(
            name="Web Development",
            description="Web development services"
        )
        self.service = Service.objects.create(
            name="Django Development",
            description="Django application development",
            category=self.category
        )

    def test_home_view(self):
        """Test the home view."""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Bienvenue dans le Gestionnaire de Services")
        self.assertContains(response, self.category.name)
        self.assertContains(response, self.service.name)

    def test_category_list_view(self):
        """Test the category list view."""
        response = self.client.get(reverse('category-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Toutes les Catégories")
        self.assertContains(response, self.category.name)

    def test_category_detail_view(self):
        """Test the category detail view."""
        response = self.client.get(reverse('category-detail', args=[self.category.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.category.name)
        self.assertContains(response, self.category.description)
        self.assertContains(response, self.service.name)

    def test_service_detail_view(self):
        """Test the service detail view."""
        response = self.client.get(reverse('service-detail', args=[self.service.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.service.name)
        self.assertContains(response, self.service.description)
        self.assertContains(response, self.category.name)

    def test_404_for_nonexistent_category(self):
        """Test 404 response for non-existent category."""
        response = self.client.get(reverse('category-detail', args=[999]))
        self.assertEqual(response.status_code, 404)

    def test_404_for_nonexistent_service(self):
        """Test 404 response for non-existent service."""
        response = self.client.get(reverse('service-detail', args=[999]))
        self.assertEqual(response.status_code, 404)
