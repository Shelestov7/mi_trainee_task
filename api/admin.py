from .models import Secret
from django.contrib import admin
from django.core import signing

class SecretAdmin(admin.ModelAdmin):
    pass



admin.site.register(Secret, SecretAdmin)
