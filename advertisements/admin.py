from django.contrib import admin
from advertisements.models import Advertisement

@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'status', 'creator', 'created_at', 'updated_at']
    model = Advertisement
    fields = ['title', 'description', 'status', 'creator', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']