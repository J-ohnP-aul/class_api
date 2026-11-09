# PythonAnywhere deployment

From a PythonAnywhere Bash console:

```bash
git clone <your-repository-url>
cd class_api
python3.13 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py check --deploy
```

In the PythonAnywhere **Web** tab, create a manual-configured web app using
the same Python version as the virtual environment. Set the virtualenv path
to `/home/<username>/class_api/.venv` and the WSGI file to:

```text
/home/<username>/class_api/cl_api/wsgi.py
```

Replace `<username>` with the PythonAnywhere account name. In that WSGI file,
before `get_wsgi_application()` is called, set the production values:

```python
os.environ['DJANGO_SECRET_KEY'] = 'generate-a-long-random-secret'
os.environ['DJANGO_DEBUG'] = 'False'
os.environ['DJANGO_ALLOWED_HOSTS'] = '<username>.pythonanywhere.com'
os.environ['DJANGO_CSRF_TRUSTED_ORIGINS'] = 'https://<username>.pythonanywhere.com'
```

Add `/home/<username>/class_api/staticfiles/` as the static files directory
with URL `/static/` in the Web tab, then reload the web app after changes.
