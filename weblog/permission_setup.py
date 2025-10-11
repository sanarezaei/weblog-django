from django.contrib.auth.models import Group, Permission

from accounts.models import User


editors_group, created = Group.objects.get_or_create(name="Editor")

permission = Permission.objects.get(codename="view_weblog_with_image")

editors_group.permissions.add(permission)
