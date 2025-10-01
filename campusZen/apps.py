"""Module de configuration de l'application CampusZen.
Ce module définit la classe CampuszenConfig, qui configure les paramètres"""

from django.apps import AppConfig


class CampuszenConfig(AppConfig):
    """
    Configuration de l'application CampusZen.
    Cette classe hérite de AppConfig et définit les paramètres de configuration
    de l'application Django 'campusZen'.

    Attributs:
        default_auto_field (str): Définit le type de clé primaire par défaut pour les modèles.
        name (str): Nom de l'application Django.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'campusZen'
