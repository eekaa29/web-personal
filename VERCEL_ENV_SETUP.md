# Vercel Environment Variables Setup

This document explains the environment variables you need to configure in Vercel for your Django application to work properly.

## Required Environment Variables

### 1. SECRET_KEY (REQUIRED)
- **Purpose**: Django's cryptographic signing key for security features
- **How to generate**: Run this command locally:
  ```bash
  python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
  ```
- **Example**: `django-insecure-abc123xyz...` (should be ~50 characters)
- **Where to set**: Vercel Dashboard → Your Project → Settings → Environment Variables
- **Scope**: Production, Preview, Development

### 2. DJANGO_ENV (REQUIRED)
- **Purpose**: Tells Django which environment it's running in
- **Value**: `production` (for production deployment)
- **Where to set**: Vercel Dashboard → Your Project → Settings → Environment Variables
- **Scope**: Production only

### 3. DEBUG (OPTIONAL)
- **Purpose**: Controls Django debug mode (only for preview/development)
- **Value**: `False` (recommended for production)
- **Where to set**: Vercel Dashboard → Your Project → Settings → Environment Variables
- **Scope**: Preview, Development (DO NOT set to True in Production)

### 4. N8N_WEBHOOK_URL (OPTIONAL)
- **Purpose**: URL for your N8N webhook integration
- **Value**: Your N8N webhook URL (e.g., `https://your-n8n-instance.com/webhook/...`)
- **Where to set**: Vercel Dashboard → Your Project → Settings → Environment Variables
- **Scope**: Production, Preview
- **Note**: If not set, webhook functionality will be disabled

## How to Set Environment Variables in Vercel

1. Go to your Vercel Dashboard: https://vercel.com/dashboard
2. Select your project
3. Click on "Settings" tab
4. Click on "Environment Variables" in the left sidebar
5. Add each variable:
   - Enter the variable name (e.g., `SECRET_KEY`)
   - Enter the value
   - Select which environments it applies to (Production/Preview/Development)
   - Click "Save"

## Verifying Your Setup

After deploying, you can verify your environment variables are set correctly:

1. Check the build logs in Vercel for any errors
2. Visit your deployed site - if you see a Django error page with details, the app is starting but has configuration issues
3. Check the Function logs in Vercel Dashboard → Your Project → Logs

## Common Issues

### Issue: "SECRET_KEY must be configured in environment variables for production"
**Solution**: Add the `SECRET_KEY` environment variable to Vercel

### Issue: "Module import errors"
**Solution**: Check that all required packages are in `requirements-production.txt`

### Issue: "500 Internal Server Error" with no details
**Solution**:
1. Check Vercel Function logs
2. Ensure `DJANGO_ENV=production` is set
3. Verify `SECRET_KEY` is set correctly

## Example .env file for local development

Create a `.env` file in your project root (this file should NOT be committed to git):

```
SECRET_KEY=your-local-secret-key-here
DJANGO_ENV=development
DEBUG=True
N8N_WEBHOOK_URL=https://your-n8n-instance.com/webhook/your-webhook-id
```

## Security Notes

- NEVER commit your `.env` file to git
- NEVER share your `SECRET_KEY` publicly
- Use different `SECRET_KEY` values for development and production
- Keep your N8N webhook URL private
