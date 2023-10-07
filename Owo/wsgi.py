"""
WSGI config for Owo project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

# 設定 Python 環境路徑
sys.path.append('home/pi/OwO/Owo/')
sys.path.append('home/pi/OwO/Owo/Owo/')

# 設定 Django settings 模組
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Owo.settings')

# 創建 WSGI 應用程式
application = get_wsgi_application()
