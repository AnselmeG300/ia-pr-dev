# 🔧 Gestionnaire de Services - Mini-Application Django

Une mini-application Django pour gérer des catégories et des services. Chaque service appartient à une catégorie, et l'application affiche la liste des catégories avec leurs services respectifs.

## 📋 Fonctionnalités

- **Gestion des Catégories** : Créer, modifier, supprimer et afficher les catégories de services
- **Gestion des Services** : Créer, modifier, supprimer et afficher les services liés à chaque catégorie  
- **Interface utilisateur** : Interface web responsive avec Bootstrap pour naviguer facilement
- **Interface d'administration** : Interface admin Django pour gérer le contenu
- **Organisation hiérarchique** : Affichage des services groupés par catégories

## 🚀 Installation et Configuration

### Prérequis
- Python 3.8+
- Django 5.0+

### Installation

1. **Cloner le repository**
   ```bash
   git clone https://github.com/AnselmeG300/ia-pr-dev.git
   cd ia-pr-dev
   ```

2. **Installer les dépendances**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configurer la base de données**
   ```bash
   python manage.py migrate
   ```

4. **Créer un superutilisateur (optionnel)**
   ```bash
   python manage.py createsuperuser
   ```

5. **Charger des données d'exemple (optionnel)**
   ```bash
   python load_sample_data.py
   ```

6. **Lancer le serveur de développement**
   ```bash
   python manage.py runserver
   ```

7. **Accéder à l'application**
   - Interface utilisateur : http://127.0.0.1:8000/
   - Interface admin : http://127.0.0.1:8000/admin/

## 🧪 Tests

Exécuter les tests unitaires :
```bash
python manage.py test
```

## 📁 Structure du Projet

```
ia-pr-dev/
├── manage.py                           # Script de gestion Django
├── requirements.txt                    # Dépendances Python
├── load_sample_data.py                 # Script de chargement des données d'exemple
├── db.sqlite3                          # Base de données SQLite
├── service_manager/                    # Configuration principale du projet Django
│   ├── __init__.py
│   ├── settings.py                     # Configuration Django
│   ├── urls.py                         # URLs principales
│   ├── wsgi.py
│   └── asgi.py
└── categories_services/                # Application principale
    ├── __init__.py
    ├── admin.py                        # Configuration de l'interface admin
    ├── apps.py
    ├── models.py                       # Modèles Category et Service
    ├── views.py                        # Vues de l'application
    ├── urls.py                         # URLs de l'application
    ├── tests.py                        # Tests unitaires
    ├── migrations/                     # Migrations de base de données
    └── templates/                      # Templates HTML
        └── categories_services/
            ├── base.html               # Template de base
            ├── home.html               # Page d'accueil
            ├── category_list.html      # Liste des catégories
            ├── category_detail.html    # Détails d'une catégorie
            └── service_detail.html     # Détails d'un service
```

## 📊 Modèles de Données

### Category (Catégorie)
- **name** : Nom de la catégorie (unique)
- **description** : Description optionnelle de la catégorie
- **created_at** : Date de création
- **updated_at** : Date de dernière modification

### Service
- **name** : Nom du service
- **description** : Description du service
- **category** : Référence vers la catégorie parente
- **created_at** : Date de création  
- **updated_at** : Date de dernière modification

## 🎯 Epics et User Stories

### Epic 1: Gestion des Catégories
**Objectif** : Permettre aux utilisateurs de voir et gérer les catégories de services

#### User Stories:
- **US1.1** : En tant qu'utilisateur, je veux voir la liste de toutes les catégories pour avoir une vue d'ensemble des types de services disponibles
- **US1.2** : En tant qu'utilisateur, je veux cliquer sur une catégorie pour voir ses détails et les services qu'elle contient
- **US1.3** : En tant qu'administrateur, je veux pouvoir ajouter une nouvelle catégorie pour organiser les services
- **US1.4** : En tant qu'administrateur, je veux pouvoir modifier une catégorie existante pour maintenir les informations à jour
- **US1.5** : En tant qu'administrateur, je veux pouvoir supprimer une catégorie vide pour maintenir l'organisation

#### Abuse User Stories:
- **AUS1.1** : En tant qu'utilisateur malveillant, je pourrais essayer d'injecter du code malveillant dans le nom d'une catégorie
- **AUS1.2** : En tant qu'utilisateur non autorisé, je pourrais essayer de supprimer des catégories importantes
- **AUS1.3** : En tant qu'utilisateur, je pourrais essayer de créer des catégories avec des noms identiques pour créer de la confusion

### Epic 2: Gestion des Services  
**Objectif** : Permettre aux utilisateurs de voir et gérer les services dans chaque catégorie

#### User Stories:
- **US2.1** : En tant qu'utilisateur, je veux voir tous les services groupés par catégorie sur la page d'accueil
- **US2.2** : En tant qu'utilisateur, je veux cliquer sur un service pour voir ses détails complets
- **US2.3** : En tant qu'administrateur, je veux pouvoir ajouter un nouveau service à une catégorie
- **US2.4** : En tant qu'administrateur, je veux pouvoir modifier un service existant
- **US2.5** : En tant qu'administrateur, je veux pouvoir déplacer un service d'une catégorie à une autre
- **US2.6** : En tant qu'administrateur, je veux pouvoir supprimer un service qui n'est plus disponible

#### Abuse User Stories:
- **AUS2.1** : En tant qu'utilisateur malveillant, je pourrais essayer d'injecter du contenu dangereux dans la description d'un service
- **AUS2.2** : En tant qu'utilisateur, je pourrais essayer d'accéder à des services qui n'existent pas ou qui ont été supprimés
- **AUS2.3** : En tant qu'utilisateur non autorisé, je pourrais essayer de créer des services sans permission

### Epic 3: Navigation et Interface Utilisateur
**Objectif** : Fournir une interface intuitive et responsive pour naviguer dans l'application

#### User Stories:
- **US3.1** : En tant qu'utilisateur, je veux une navigation claire pour passer facilement entre les pages
- **US3.2** : En tant qu'utilisateur, je veux un design responsive qui fonctionne sur mobile et desktop
- **US3.3** : En tant qu'utilisateur, je veux des liens de retour pour naviguer facilement dans la hiérarchie
- **US3.4** : En tant qu'utilisateur, je veux voir le nombre de services dans chaque catégorie

#### Abuse User Stories:
- **AUS3.1** : En tant qu'utilisateur, je pourrais essayer d'accéder à des URLs non existantes pour provoquer des erreurs
- **AUS3.2** : En tant qu'utilisateur, je pourrais essayer de naviguer sans JavaScript activé et casser l'interface

## 🔒 Mesures de Sécurité Implémentées

- **Protection CSRF** : Django CSRF protection activée
- **Validation des données** : Validation des modèles Django
- **Échappement HTML** : Protection automatique contre XSS
- **Interface Admin sécurisée** : Authentification requise pour l'administration
- **Contraintes de base de données** : Contraintes d'unicité et de référence

## 🛠️ Technologies Utilisées

- **Backend** : Django 5.2.6, Python 3.12
- **Frontend** : HTML5, CSS3, Bootstrap 5.1.3
- **Base de données** : SQLite (développement)
- **Tests** : Django TestCase

## 🤝 Contribution

1. Fork le projet
2. Créer une branche pour votre fonctionnalité (`git checkout -b feature/AmazingFeature`)
3. Commit vos changements (`git commit -m 'Add some AmazingFeature'`)
4. Push vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrir une Pull Request

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.