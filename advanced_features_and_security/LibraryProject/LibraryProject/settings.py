# Security settings for the Django application
import os

# ------------- Django Security Settings -------------

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

# Redirect all HTTP to HTTPS
SECURE_REDIRECT_EXEMPT = []  # Optional for specific exclusions
