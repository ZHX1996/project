import os
import django
from django.contrib.auth.models import Permission, User

django.setup()
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "www.settings")
if django.VERSION >= (1, 7):
    django.setup()

User.objects.get(username='').user_permissions.values()