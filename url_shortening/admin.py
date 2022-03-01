from django.contrib import admin
from .models import URL
# Register your models here.

@admin.register(URL)
class URLModelAdmin(admin.ModelAdmin):

    list_display = ('short_url','total_clicks','created_at')
    list_filter = ('created_at',)
    list_display_links = ('short_url',)
    ordering = ('-created_at',)
    readonly_fields = ['short_url','total_clicks']
