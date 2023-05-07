#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

# + Создать проект Django.
# + Добавить в него 3 статические странички.
# + На одной из страниц контент повторяется 2 раза без изменения content (два раза прописано {{ flatpage.content }}).
# + Одна из страниц на сайте доступна только админу (только вошедшему пользователю).
# + На одной из страниц изменены шрифты и размеры текста.
# + Сайт представляет собой оформленный Bootstrap-шаблон со встроенными пользовательскими данными.
# + Статические файлы Bootstrap загружаются через теги {% load static %} и {% static %}