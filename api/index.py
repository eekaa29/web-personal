# api/index.py
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web_personal.settings")

# La app WSGI que Vercel invoca
app = get_wsgi_application()
