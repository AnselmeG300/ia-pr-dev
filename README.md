# Django Services Management Application

Une mini-application Django pour gérer des catégories et des services. Chaque service appartient à une catégorie, et l'application affiche la liste des catégories avec leurs services respectifs.

## Fonctionnalités

- **Gestion des catégories** : Créer, modifier et supprimer des catégories de services
- **Gestion des services** : Créer, modifier et supprimer des services dans chaque catégorie
- **Interface publique** : Affichage des catégories et services pour les visiteurs
- **Interface d'administration** : Gestion complète via Django Admin

## Modèles de données

### Category (Catégorie)
- `name` : Nom de la catégorie (unique)
- `description` : Description de la catégorie
- `created_at` / `updated_at` : Timestamps

### Service
- `name` : Nom du service
- `description` : Description du service
- `category` : Relation vers une catégorie (ForeignKey)
- `price` : Prix du service (optionnel)
- `is_active` : Statut actif/inactif
- `created_at` / `updated_at` : Timestamps

## Installation et utilisation

### Prérequis
- Python 3.8+
- Django 5.2+

### Installation
1. Installer les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

2. Appliquer les migrations :
   ```bash
   python manage.py migrate
   ```

3. Créer un superutilisateur :
   ```bash
   python manage.py createsuperuser
   ```

4. Démarrer le serveur de développement :
   ```bash
   python manage.py runserver
   ```

### Utilisation
- **Page d'accueil** : `http://localhost:8000/` - Liste toutes les catégories avec leurs services
- **Page catégorie** : `http://localhost:8000/category/<id>/` - Affiche les services d'une catégorie spécifique
- **Administration** : `http://localhost:8000/admin/` - Interface d'administration Django

## Structure du projet

```
services_management/          # Projet Django principal
├── settings.py              # Configuration Django
├── urls.py                  # URLs principales
└── wsgi.py                  # Configuration WSGI

services/                    # Application Django
├── models.py               # Modèles Category et Service
├── views.py                # Vues pour l'affichage
├── admin.py                # Configuration Django Admin
├── urls.py                 # URLs de l'application
└── templates/services/     # Templates HTML
    ├── base.html          # Template de base
    ├── category_list.html # Liste des catégories
    └── category_detail.html # Détail d'une catégorie
```

## Exemples de données

L'application inclut des exemples de catégories :
- **Développement Web** : Sites vitrines, applications web, e-commerce
- **Marketing Digital** : SEO, Google Ads, réseaux sociaux
- **Design Graphique** : Logos, chartes graphiques, supports de communication
- **Conseil** : Audits techniques, stratégie digitale

## Interface utilisateur

L'interface est volontairement simple et fonctionnelle avec :
- Design responsive
- Navigation intuitive
- Affichage clair des informations
- Liens vers l'administration Django