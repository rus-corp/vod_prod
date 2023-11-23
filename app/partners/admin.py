from django.contrib import admin

from .models import Partner, Client

@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']