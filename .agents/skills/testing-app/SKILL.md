# Testing nelsonblog Django App

## Local Setup for Testing

1. **Install dependencies**:
   ```bash
   pip install django python-decouple django-cleanup Pillow
   ```

2. **Create `.env` file** in project root:
   ```
   SECRET_KEY=test-secret-key-for-local-dev-only-12345
   DEBUG=True
   EMAIL_HOST=smtp.gmail.com
   EMAIL_PORT=587
   EMAIL_USE_TLS=True
   EMAIL_HOST_USER=test@test.com
   EMAIL_HOST_PASSWORD=testpassword
   ```

3. **Temporarily modify `Nelsonblog/settings.py`** for local testing (do NOT commit these changes):
   - Switch database from PostgreSQL to SQLite:
     ```python
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.sqlite3',
             'NAME': BASE_DIR / 'db_test.sqlite3',
         }
     }
     ```
   - Switch email backend to console:
     ```python
     EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
     ```
   - Add localhost to ALLOWED_HOSTS:
     ```python
     ALLOWED_HOSTS = ['localhost', '127.0.0.1']
     ```

4. **Run migrations and seed data**:
   ```bash
   python manage.py makemigrations && python manage.py migrate
   python manage.py collectstatic --noinput
   ```
   Then seed test users, categories, and articles via a Python script.
   - Create at least one user WITH a profile but NO photo (to test photo guard)
   - Create at least one user WITHOUT a profile at all
   - Create articles by both users to test article_detail template guards

5. **Start dev server**:
   ```bash
   python manage.py runserver 8000
   ```

6. **Restore settings after testing**:
   ```bash
   git checkout -- Nelsonblog/settings.py
   ```

## Key URLs

- Index: `http://127.0.0.1:8000/`
- Login: `http://127.0.0.1:8000/user/login/`
- Register: `http://127.0.0.1:8000/user/add/`
- Article detail: `http://127.0.0.1:8000/article/<slug>`
- Admin: `http://127.0.0.1:8000/admin/`

## Known Issues

- **Logout on Django 6.0**: The logout link uses `<a href>` which gives a 405 error because Django 6.0 requires POST for logout. This is a pre-existing issue in the app's `menu.html` template — the logout link should be a `<form>` with POST method.
- **Session clearing**: Django uses httponly cookies, so you can't clear sessions via JavaScript. Use `Session.objects.all().delete()` via the Django shell or management command to log out all users.
- **DEBUG setting bug**: The `config('DEBUG', 'cast=bool')` call might not parse correctly — the string `'cast=bool'` is the default value, not a keyword argument. This was reported in PR #1.
- **STATICFILES_DIR vs STATICFILES_DIRS**: The setting should be `STATICFILES_DIRS` (plural). This was reported in PR #1.

## Testing Responsive CSS

- Use Chrome DevTools device toolbar (F12 → click device icon or Ctrl+Shift+M)
- Test at these breakpoints:
  - Mobile: 375-400px wide
  - Tablet: 768-1023px wide  
  - Desktop: 1024px+ wide
- Key things to verify:
  - Hamburger menu appears below 1024px
  - Hamburger toggle opens/closes nav
  - Article cards: 1 column mobile, 2 columns tablet, multi-column desktop
  - Forms: ~90% width mobile, ~60% tablet, ~30% desktop

## Devin Secrets Needed

None required for local testing. The app uses a local `.env` file with test values.
