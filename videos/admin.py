from django.contrib import admin

# Register your models here.

from .models import video, Category


class videoAdmin(admin.ModelAdmin):
    list_display = ["__str__", "slug"]
    fields = ["title", "slug", "embed_code", "share_message", "image", "active", "featured", "free_preview", "category", "product_img", "product_embed",]
    prepopulated_fields = {'slug': ["title",]}  
    class Meta:
        model = video


admin.site.register(video, videoAdmin)
admin.site.register(Category)

