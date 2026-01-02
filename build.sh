#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

echo "========================================="
echo "Vercel Build Script - Starting"
echo "========================================="

# Display Python version for debugging
echo "Python version:"
python --version

# Install Python dependencies
echo "Installing Python dependencies..."
pip install -r requirements-production.txt

# Display Django version for debugging
echo "Django version:"
python -c "import django; print(django.get_version())"

# Check if manage.py exists
if [ ! -f "manage.py" ]; then
    echo "ERROR: manage.py not found!"
    exit 1
fi

# Create static files directory
echo "Creating static files directory..."
mkdir -p public/static
echo "✓ Directory created: public/static"

# Run collectstatic
echo "Running collectstatic..."
python manage.py collectstatic --noinput --clear --verbosity 2

echo "========================================="
echo "✓ Build completed successfully!"
echo "========================================="
