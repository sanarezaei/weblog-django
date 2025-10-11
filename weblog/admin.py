from django.contrib import admin

from .models import Tag, Weblog

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name", )

@admin.register(Weblog)
class WeblogAdmin(admin.ModelAdmin):
    list_display = ("title", "author", )

    def has_view_permission(self, request, obj=None ):
        if request.user.is_superuser:
            return True
        
        return request.user.has_perm("weblog.view_weblog_with_image")
