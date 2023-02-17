from django.contrib import admin
from .models import Credential

class CredentialAdmin(admin.ModelAdmin):
    list_display = ['credential_for','username','password', 'url', 'is_active', 'owner']
    fields = ['owner','credential_for','description','featured_image', 'username','password', 'url', 'is_active']

admin.site.register(Credential, CredentialAdmin)

