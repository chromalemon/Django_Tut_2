from django.contrib import admin

# Register your models here.

from .models import LogMessage
admin.site.register(LogMessage)