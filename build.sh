#!/bin/bash

# Script de build para Vercel
echo "Ejecutando collectstatic..."

# Asegurarse de que el directorio de archivos estáticos existe
mkdir -p public/static

# Ejecutar collectstatic sin input del usuario
python manage.py collectstatic --noinput

echo "Build completado exitosamente"
