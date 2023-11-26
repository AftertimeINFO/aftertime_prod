#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
# ---------------------- STANDARD LIBRARIES ----------------------
import os
import sys
# ---------------------- EXTERNAL LIBRARIES ----------------------
from dotenv import load_dotenv


def main():
    """Run administrative tasks."""
    load_dotenv()
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django.                                                                                                                                                                                                                                                                                              m                                                       Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    if sys.argv[1] == "init":
        print("Initialization ongoing.")
        from config.settings._general import *
    else:
        main()
