#!/usr/bin/env python3
"""Script to load sample data for the Django application."""

import os
import sys
import django

# Add the project path to Python path
sys.path.append('/home/runner/work/ia-pr-dev/ia-pr-dev')

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'service_manager.settings')
django.setup()

from categories_services.models import Category, Service

def load_sample_data():
    """Load sample categories and services."""
    
    # Create categories
    categories_data = [
        {
            'name': 'Développement Web',
            'description': 'Services liés au développement d\'applications web et sites internet'
        },
        {
            'name': 'Design Graphique',
            'description': 'Services de création graphique, logos, identité visuelle'
        },
        {
            'name': 'Marketing Digital',
            'description': 'Services de marketing en ligne, SEO, réseaux sociaux'
        },
        {
            'name': 'Consultation IT',
            'description': 'Services de conseil en informatique et technologie'
        }
    ]
    
    created_categories = []
    for cat_data in categories_data:
        category, created = Category.objects.get_or_create(
            name=cat_data['name'],
            defaults={'description': cat_data['description']}
        )
        created_categories.append(category)
        print(f"{'Créée' if created else 'Existe déjà'}: {category.name}")
    
    # Create services
    services_data = [
        # Développement Web
        {
            'name': 'Développement Django',
            'description': 'Création d\'applications web avec le framework Django Python',
            'category': 'Développement Web'
        },
        {
            'name': 'Développement React',
            'description': 'Développement d\'interfaces utilisateur avec React.js',
            'category': 'Développement Web'
        },
        {
            'name': 'API REST',
            'description': 'Création d\'APIs RESTful pour applications web et mobiles',
            'category': 'Développement Web'
        },
        
        # Design Graphique
        {
            'name': 'Création de Logo',
            'description': 'Conception de logos professionnels et identité de marque',
            'category': 'Design Graphique'
        },
        {
            'name': 'Design UI/UX',
            'description': 'Conception d\'interfaces utilisateur et expérience utilisateur',
            'category': 'Design Graphique'
        },
        
        # Marketing Digital
        {
            'name': 'Optimisation SEO',
            'description': 'Amélioration du référencement naturel de votre site web',
            'category': 'Marketing Digital'
        },
        {
            'name': 'Gestion Réseaux Sociaux',
            'description': 'Animation et gestion de vos comptes sur les réseaux sociaux',
            'category': 'Marketing Digital'
        },
        
        # Consultation IT
        {
            'name': 'Audit Sécurité',
            'description': 'Analyse et audit de sécurité de vos systèmes informatiques',
            'category': 'Consultation IT'
        },
        {
            'name': 'Architecture Système',
            'description': 'Conception et optimisation d\'architectures système',
            'category': 'Consultation IT'
        }
    ]
    
    for service_data in services_data:
        category = Category.objects.get(name=service_data['category'])
        service, created = Service.objects.get_or_create(
            name=service_data['name'],
            category=category,
            defaults={'description': service_data['description']}
        )
        print(f"{'Créé' if created else 'Existe déjà'}: {service.name}")
    
    print(f"\nRésumé:")
    print(f"Catégories: {Category.objects.count()}")
    print(f"Services: {Service.objects.count()}")

if __name__ == '__main__':
    load_sample_data()