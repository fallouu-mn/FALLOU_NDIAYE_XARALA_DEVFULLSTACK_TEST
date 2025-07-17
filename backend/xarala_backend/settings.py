from pathlib import Path

# === Chemin de base ===
BASE_DIR = Path(__file__).resolve().parent.parent

# === Sécurité ===
SECRET_KEY = 'django-insecure-twuop7ck_z7d^chfrbgd2mb@szudff4d$je8tko4lkrqu!b(^7'
DEBUG = True  # ❗ Mets à False en production

# ✅ Autorise Render et développement local
ALLOWED_HOSTS = ['xarala-backend.onrender.com', 'localhost', '127.0.0.1']

# === Applications installées ===
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Apps supplémentaires
    'rest_framework',
    'corsheaders',      # Ajouté pour CORS
    'bootcamps',        # Ton app principale
]

# === Middleware ===
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',  # doit être AVANT CommonMiddleware
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ✅ Autorise les appels API depuis ton frontend Netlify
CORS_ALLOWED_ORIGINS = [
    "https://papaya-praline-f0f58e.netlify.app",  # frontend React déployé
]

# === URLs principales ===
ROOT_URLCONF = 'xarala_backend.urls'

# === Templates ===
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

# === WSGI ===
WSGI_APPLICATION = 'xarala_backend.wsgi.application'

# === Base de données ===
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# === Validation des mots de passe ===
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# === Internationalisation ===
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# === Fichiers statiques ===
STATIC_URL = 'static/'

# === Type de clé primaire par défaut ===
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
