#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
<<<<<<< HEAD
=======
    """Run administrative tasks."""
>>>>>>> 30c7d3d263f020e02fa82aeeba7f2e4c7a4ec528
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'financeblog.settings')
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
