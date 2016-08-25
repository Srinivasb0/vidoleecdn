from django.contrib import admin

# Register your models here.

from .models import Resource

class ResourceAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_by')
    date_hierarchy = 'created_at'
    search_field = ['title', 'url']


admin.site.register(Resource, ResourceAdmin)