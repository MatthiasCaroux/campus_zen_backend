# settings du projet django
# fichier surtout utile pour la config globale

from pathlib import Path
from datetime import timedelta

# chemin de base du projet
BASE_DIR = Path(__file__).resolve().parent.parent


# config pour le dev

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-lcpljd52dld)6=2v^=7#*95nsl9j12m^df@=fph5#ddxo9_op$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']  # Autorise tous les hôtes 



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'campusZen',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # WhiteNoise pour servir les fichiers statiques
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'campusZen.middleware.JWTCookieAuthenticationMiddleware',  # Middleware JWT cookies
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'campus_zen_backend.urls'

# Configuration CORS pour cookies HttpOnly
# IMPORTANT: CORS_ALLOW_ALL_ORIGINS ne peut PAS être True avec CORS_ALLOW_CREDENTIALS
CORS_ALLOW_ALL_ORIGINS = False

# Permet l'envoi de cookies avec les requetes CORS (pour HttpOnly cookies)
CORS_ALLOW_CREDENTIALS = True

CORS_ALLOWED_ORIGINS = [
    'http://localhost:5173',
    'http://127.0.0.1:5173',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'campus_zen_backend.wsgi.application'


# base de donnees

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# validation des mots de passe

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# langue et timezone

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# fichiers statiques

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# WhiteNoise configuration pour la compression et le cache
STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

AUTH_USER_MODEL = 'campusZen.Personne'

# type de cle primaire par defaut

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=60),
    # "ACCESS_TOKEN_LIFETIME": timedelta(hours=5),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=60),
    "AUTH_HEADER_TYPES": ("Bearer",),
    "USER_ID_FIELD": "idPers",
    "USER_ID_CLAIM": "user_id",
    
    # Support des cookies HttpOnly (optionnel, gere manuellement dans la vue)
    "AUTH_COOKIE": "access_token",
    "AUTH_COOKIE_SECURE": False,  # Mettre True en production avec HTTPS
    "AUTH_COOKIE_HTTP_ONLY": True,
    "AUTH_COOKIE_SAMESITE": "Lax",
}

