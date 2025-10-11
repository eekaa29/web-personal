#!/usr/bin/env bash
set -euo pipefail

pip install -r requirements.txt

# Tailwind / Node
cd theme
npm ci
cd ..

# Compila CSS y recoge estáticos
python manage.py tailwind build
python manage.py collectstatic --noinput
