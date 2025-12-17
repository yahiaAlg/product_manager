# PROJECT STRUCTURE
```
product_manager/
├── manage.py
├── requirements.txt
├── product_manager/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── products/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── migrations/
│       └── __init__.py
├── templates/
│   ├── base.html
│   ├── products/
│   │   ├── product_list.html
│   │   ├── product_form.html
│   │   └── product_confirm_delete.html
│   └── service-worker.js
└── static/
    ├── css/
    │   └── style.css
    ├── js/
    │   └── app.js
    └── pwa/
        ├── manifest.json
        ├── icon-192.png
        └── icon-512.png
```



# SETUP INSTRUCTIONS

1. Create project directory:
   `mkdir product_manager && cd product_manager`

2. Create virtual environment:
   `python -m venv venv`
   `source venv/bin/activate  # On Windows: venv\\Scripts\\activate`

3. Install Django:
   `pip install django`

4. Create Django project:
   `django-admin startproject product_manager .`

5. Create products app:
   `python manage.py startapp products`

6. Replace files with content above

7. Create icon files (192x192 and 512x512 PNG):
   - Use online generator or create simple colored squares
   - Save as static/pwa/icon-192.png and static/pwa/icon-512.png

8. Run migrations:
   `python manage.py makemigrations`
   `python manage.py migrate`

9. Create superuser:
   `python manage.py createsuperuser`

10. Run server:
    `python manage.py runserver`

11. Access at http://localhost:8000

**TO GENERATE APK:**
**Use ngrok for HTTPS testing, then use PWABuilder.com or Bubblewrap CLI**

```bash
bubblewrap init --manifest https://127.0.0.1:8000/static/pwa/manifest.json
```
