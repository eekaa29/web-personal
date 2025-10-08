from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
import json, os, requests
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

class HomeView(TemplateView):
    template_name = "core/home.html"

class ProjectsView(TemplateView):
    template_name= "core/projects.html"

class CommunityView(TemplateView):
    template_name= "core/community.html"

class ContentView(TemplateView):
    template_name= "core/content.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["workflows"] = [
            {
                "title": "Contacto → Google Sheets + Email",
                "desc": "Guarda leads en Sheets y envía notificación por email.",
                # opcional: si quieres ofrecer importación por URL desde GitHub:
                "github_raw": "https://raw.githubusercontent.com/tuuser/tu-repo/main/workflows/contacto-v1/workflow.json",
            },
            {
                "slug": "newsletter-v1",
                "title": "Newsletter → MailerLite",
                "desc": "Añade suscriptores y etiqueta por origen.",
                "github_raw": None,
            },
        ]
        return ctx

class ContactView(TemplateView):
    template_name= "core/contact.html"

N8N_WEBHOOK_URL = getattr(settings, "N8N_WEBHOOK_URL", "")

@require_POST
def contact_api(request):
    # Si mandas JSON desde el front:
    try:
        data = json.loads(request.body.decode("utf-8"))
    except Exception:
        data = request.POST.dict()  # fallback si envías form-data

    # Honeypot anti-bots
    if data.get("website"):  # campo oculto
        return JsonResponse({"ok": True})  # silenciosamente OK

    payload = {
        "name": data.get("name", ""),
        "email": data.get("email", ""),
        "phone": data.get("phone", ""),
        "source": "website",
        "ip": request.META.get("REMOTE_ADDR"),
        "ua": request.META.get("HTTP_USER_AGENT"),
    }

    try:
        r = requests.post(N8N_WEBHOOK_URL, json=payload, timeout=7)
        r.raise_for_status()
        return JsonResponse({"ok": True})
    except requests.RequestException as e:
        return JsonResponse({"ok": False, "error": "n8n upstream failed"}, status=502)
