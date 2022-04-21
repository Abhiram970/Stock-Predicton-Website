from django.contrib import admin

from register.views import register

# Register your models here.
from .models import page2

admin.site.register(page2)