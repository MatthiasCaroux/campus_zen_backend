# CampusZen Backend - API REST Django

<div align="center">

**Backend API** pour la plateforme CampusZen

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-4.2-green.svg)](https://www.djangoproject.com/)
[![DRF](https://img.shields.io/badge/DRF-3.16-brightgreen.svg)](https://www.django-rest-framework.org/)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](../LICENSE)

</div>

## 📋 Table des matières

- [Aperçu](#-aperçu)
- [Prérequis](#-prérequis)
- [Installation](#-installation)
- [Mise en production (OVH)](#-mise-en-production-ovh)
- [API Endpoints](#-api-endpoints)
- [Modèles de données](#-modèles-de-données)
- [Tests](#-tests)
- [Dépannage](#-dépannage)

## 🎯 Aperçu

CampusZen Backend est une **API REST complète** construite avec Django et Django REST Framework :

✅ Gestion complète des questionnaires et questions  
✅ Authentification sécurisée (JWT + Cookies HttpOnly)  
✅ Gestion des utilisateurs (étudiants, administrateurs)  
✅ Calcul automatique des résultats  
✅ Gestion des ressources et contacts professionnels  
✅ Base de données SQLite/PostgreSQL  

## 📦 Prérequis

- **Python** 3.8 ou supérieur
- **pip** (gestionnaire de paquets Python)
- **Git**
- **Docker** et **Docker Compose** (optionnel)

## 🚀 Installation

### 1. Cloner et configurer

```bash
git clone https://github.com/MatthiasCaroux/campus_zen_backend.git
cd campus_zen_backend
python -m venv venv
# Windows: venv\Scripts\activate
# macOS/Linux: source venv/bin/activate
```

### 2. Installer et lancer

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

**API disponible à** : `http://localhost:8000`  
**Admin Django** : `http://localhost:8000/admin`

## 🚀 Mise en production (OVH)

Le serveur est configuré pour prendre en compte le fait que le backend se lance sur `http://127.0.0.1:8000`.

### Déploiement recommandé

1. Cloner le backend dans le dossier home du serveur (ex: `/home/ubuntu`).
2. Installer les dépendances Python.
3. Suivre les indications du README présent dans le home.

### Guide Screen pour API Django

#### Lancer l'API

```bash
#!/bin/bash
source /home/ubuntu/venv/bin/activate
cd /home/ubuntu/campus_zen_backend
gunicorn campus_zen_backend.wsgi:application --bind 127.0.0.1:8000 --workers 3
```

#### Commandes utiles

```bash
# Voir les sessions actives
screen -ls

# Se reconnecter pour voir les logs
screen -r django-api

# Se reconnecter en forçant le détachement
screen -d -r django-api

# Supprimer une session
screen -S django-api -X quit
```

#### Raccourcis

- **Ctrl+A puis D** : Détacher la session
- **Ctrl+A puis K** : Tuer la session (confirmer avec Y)

### Démarrage via script

Dans le screen, il est recommandé de lancer le script `start_api.sh` situé dans le home.

### Sur un navigateur

Pour consulter l'API depuis un navigateur, ouvrez : `https://incidents-bouake.com/api/`

## 🔌 API Endpoints

### Endpoints principaux

- `GET/POST /api/questionnaires/` - Questionnaires
- `GET/POST /api/questions/` - Questions
- `GET/POST /api/reponses/` - Réponses
- `GET/POST /api/personnes/` - Utilisateurs
- `GET/POST /api/ressources/` - Ressources
- `GET/POST /api/professionnels/` - Professionnels
- `GET/POST /api/climats/` - États émotionnels

### Authentification

Pour accéder aux endpoints, utiliser un token JWT obtenu lors de la connexion. Les tokens sont automatiquement gérés via cookies HttpOnly.

### Soumission de questionnaire

L'endpoint `/api/submit-questionnaire/` permet de soumettre les réponses d'un questionnaire et de recevoir les résultats avec recommandations.

## 📊 Modèles de données

| Modèle | Description |
|--------|-------------|
| **Personne** | Utilisateurs (étudiants, admins) |
| **Questionnaire** | Questionnaires de bien-être |
| **Question** | Questions des questionnaires |
| **Réponse** | Réponses possibles (Likert 1-7) |
| **SubmitRecu** | Soumissions complétées |
| **Ressource** | Articles, vidéos, ressources |
| **Professionnel** | Professionnels de santé |
| **Climat** | États émotionnels (résultats) |
| **Message** | Messages d'encouragement |

## 🧪 Tests

Le projet inclut une suite de tests complète couvrant tous les endpoints API. Les tests utilisent Django TestCase avec des données de test.

**Exécution des tests :**
- Exécuter tous les tests avec `python manage.py test`
- Générer un rapport de couverture avec `coverage run --source='campusZen' manage.py test`
- Voir le rapport détaillé en HTML avec `coverage html`
- Un script automatisé `launchTests.sh` est disponible pour faciliter l'exécution

## 🔐 Sécurité

✅ JWT avec Cookies HttpOnly  
✅ CORS configuré  
✅ Validation complète des données  
✅ Hachage des mots de passe  
✅ Protection CSRF activée  

## 🔧 Dépannage

### Migrations non appliquées

Exécuter `python manage.py migrate` pour appliquer les migrations en attente.

### Module non trouvé

Réinstaller les dépendances avec `pip install -r requirements.txt`.

### Port déjà utilisé

Lancer le serveur sur un port différent, par exemple le port 8001.

## 📚 Ressources

- [Django Docs](https://docs.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Django SimpleJWT](https://github.com/jpadilla/django-rest-framework-simplejwt)

## Auteurs
- Enzo Familiar-Marais
- Matthias Caroux
- Niksan Nagarajah
- Samuel Niveau

## 📝 License

MIT - Voir [LICENSE](../LICENSE)

