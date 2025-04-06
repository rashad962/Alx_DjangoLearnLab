# Django Security Review – LibraryProject

## Configured Security Settings (in `settings.py`)

- **`SECURE_SSL_REDIRECT=True`**: Redirects all HTTP to HTTPS.
- **`SECURE_HSTS_SECONDS=31536000`**: Enables HSTS for 1 year.
- **`SECURE_HSTS_INCLUDE_SUBDOMAINS=True`**: Applies HSTS to all subdomains.
- **`SECURE_HSTS_PRELOAD=True`**: Opts into browser preload lists.
- **`SECURE_CONTENT_TYPE_NOSNIFF=True`**: Prevents MIME-sniffing attacks.
- **`SECURE_BROWSER_XSS_FILTER=True`**: Enables browser-based XSS protection.
- **`X_FRAME_OPTIONS='DENY'`**: Mitigates clickjacking by preventing iframe embedding.
- **`SESSION_COOKIE_SECURE=True`, `CSRF_COOKIE_SECURE=True`**: Ensures cookies are only sent over HTTPS.
- **`DEBUG=False`**: Ensures sensitive information is never shown in production.

## Deployment Security (Nginx)

- HTTP is redirected to HTTPS using `return 301`.
- SSL certificates provided via Let's Encrypt.
- HSTS headers are set at the web server level to enforce HTTPS.

## Recommendations

- Regularly rotate and monitor your TLS/SSL certificates.
- Add Content Security Policy (CSP) headers using the `django-csp` package.
- Enable logging for suspicious activity and failed login attempts.
- If behind a reverse proxy (e.g., Heroku, Nginx), set `SECURE_PROXY_SSL_HEADER`.

