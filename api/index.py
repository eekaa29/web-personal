# api/index.py
import os
import sys
from pathlib import Path

# Add the project root to Python path
project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))

# Set Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web_personal.settings")

# Enable Django debugging for startup errors (will be disabled by settings.py in production)
os.environ.setdefault("DJANGO_DEBUG_STARTUP", "1")

try:
    from django.core.wsgi import get_wsgi_application

    # Initialize Django application
    app = get_wsgi_application()

except Exception as e:
    # If Django fails to start, create a simple WSGI app that shows the error
    import traceback

    error_message = f"""
    <html>
    <head><title>Django Startup Error</title></head>
    <body>
        <h1>Django Application Failed to Start</h1>
        <h2>Error: {str(e)}</h2>
        <pre>{traceback.format_exc()}</pre>
        <hr>
        <p>Check your Vercel logs for more details.</p>
        <p>Common issues:</p>
        <ul>
            <li>Missing environment variables (SECRET_KEY, DJANGO_ENV)</li>
            <li>Module import errors</li>
            <li>Database configuration issues</li>
        </ul>
    </body>
    </html>
    """

    def app(environ, start_response):
        status = '500 Internal Server Error'
        headers = [('Content-Type', 'text/html')]
        start_response(status, headers)
        return [error_message.encode('utf-8')]

    # Also print to stderr for Vercel logs
    print(f"CRITICAL ERROR: Django failed to start: {e}", file=sys.stderr)
    print(traceback.format_exc(), file=sys.stderr)
