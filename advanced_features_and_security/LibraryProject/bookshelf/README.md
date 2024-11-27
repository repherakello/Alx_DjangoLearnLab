# Security Measures Implemented

## 1. Secure Settings
- `DEBUG` is set to `False` in production.
- Cookie security enforced (`CSRF_COOKIE_SECURE`, `SESSION_COOKIE_SECURE`).
- HTTP to HTTPS redirection (`SECURE_SSL_REDIRECT`).
- HSTS is enabled with a 1-year duration (`SECURE_HSTS_SECONDS`).

## 2. CSRF Protection
- All forms include `{% csrf_token %}` to protect against CSRF attacks.

## 3. Secure Data Access
- Views use Django’s ORM to prevent SQL injection.
- User input is validated before being used in queries.

## 4. Content Security Policy (CSP)
- A CSP header is configured using the `django-csp` middleware to control which sources are allowed for scripts, styles, and images.

## Testing Approach:
- Manually tested form submissions to ensure CSRF protection is in place.
- Tested search functionality with various inputs to confirm secure handling of data.
