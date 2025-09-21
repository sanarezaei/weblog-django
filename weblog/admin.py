from django.contrib import admin

from .models import Tag, Weblog

admin.site.register(Weblog)
admin.site.register(Tag)
