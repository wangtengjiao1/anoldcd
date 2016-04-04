# -*- coding: utf-8 -*-
# __author__ = 'neo'
# __name__ = '王腾蛟'
# __time__ = '2015年,上午1:48'
# ____________________分割线___________________
"""
WSGI config for basic project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "main.settings")

application = get_wsgi_application()
