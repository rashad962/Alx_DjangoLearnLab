# Django settings for LibraryProject

import os

# ------------- SECURITY CONFIGURATIONS -------------

# Disable debug mode in production for security
DEBUG = False

# Define allowed hosts for security
ALLOWED_HOSTS = ['yourdomain.com']  # Replace with your actual domain

# Enforce HTTPS
SECURE_SSL_REDIRECT = True  # Enforces redirect from HTTP to HTTPS

# HTTP Strict Transport Security (HSTS)
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True  # Apply to all subdomains
SECURE_HSTS_PRELOAD = True  # Allow browser preload list

# Prevent browsers from MIME-sniffing content
SECURE_CONTENT_TYPE_NOSNIFF = True

# Enable browser XSS filtering to prevent XSS attacks
SECURE_BROWSER_XSS_FILTER = True

# Prevent clickjacking attacks by denying iframe embedding
X_FRAME_OPTIONS = 'DENY'

# Secure session and CSRF cookies - ensure they are transmitted over HTTPS
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Enforce HTTPS for all cookies
SECURE_REDIRECT_EXEMPT = []  # Optional for specific exclusions

# Reverse Proxy handling settings (for when behind a proxy like Nginx)
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Enforce that HTTP request is redirected to HTTPS in production
SECURE_BROWSER_XSS_FILTER = True

# ------------- DATABASE CONFIGURATION -------------
# Example database configuration (update as per your settings)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_database_name',
        'USER': 'your_database_user',
        'PASSWORD': 'your_database_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# ------------- STATIC & MEDIA FILE CONFIGURATION -------------
STATIC_URL = '/static/'
MEDIA_URL = '/media/'

# ------------- INTERNATIONALIZATION -------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'

USE_I18N = True
USE_L10N = True
USE_TZ = True

# ------------- APPLICATION CONFIGURATION -------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'csp',  # If you're using Content Security Policy (CSP)
    # Add your apps here
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'csp.middleware.CSPMiddleware',  # If you're using CSP
    # Add other middleware as required
]

ROOT_URLCONF = 'LibraryProject.urls'

# ------------- WSGI CONFIGURATION -------------
WSGI_APPLICATION = 'LibraryProject.wsgi.application'

# ------------- TEMPLATES CONFIGURATION -------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# ------------- AUTHENTICATION CONFIGURATION -------------
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

# ------------- SECURITY HEADER SETTINGS -------------
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'
SECURE_BROWSER_XSS_FILTER = True

# ------------- CSP (Content Security Policy) SETTINGS -------------
CSP_DEFAULT_SRC = ("'self'",)
CSP_SCRIPT_SRC = ("'self'", "https://trusted.cdn.com")  # Add trusted script sources
CSP_STYLE_SRC = ("'self'", "https://trusted.cdn.com")   # Add trusted style sources

# ------------- CSRF & SESSION SETTINGS -------------
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

# ------------- LOGGING CONFIGURATION -------------
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

# ------------- SSL REDIRECT & SECURE HEADERS -------------
SECURE_SSL_REDIRECT = True  # Enforces redirect from HTTP to HTTPS
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True  # Apply to all subdomains
SECURE_HSTS_PRELOAD = True  # Allow browser preload list

# Ensure SSL headers are passed when behind a reverse proxy
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
