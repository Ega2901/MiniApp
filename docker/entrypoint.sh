#!/bin/bash
set -e

# Применение миграций
poetry run python manage.py migrate

# Запуск сервера
poetry run python manage.py runserver 0.0.0.0:8000
