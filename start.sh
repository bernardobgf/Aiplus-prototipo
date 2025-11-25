#!/usr/bin/env bash
# Script para iniciar o serviço no Render de forma robusta
set -o errexit

echo "Executando migrações..."
python manage.py migrate

echo "Coletando arquivos estáticos..."
python manage.py collectstatic --noinput

echo "Iniciando Gunicorn..."
gunicorn config.wsgi:application --bind 0.0.0.0:$PORT