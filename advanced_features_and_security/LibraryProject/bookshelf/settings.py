# Add these to your existing settings.py

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users.apps.UsersConfig',  # Make sure this comes before django.contrib.auth
    # ... any other apps ...
]

AUTH_USER_MODEL = 'users.CustomUser'

# Add at the bottom of the file
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')