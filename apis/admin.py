from django.contrib import admin
from .models import App
import hashlib
# Register your models here.

# admin.site.register(App)

@admin.register(App)
class ApisAppAdmin(admin.ModelAdmin):
    fields = ['name', 'application', 'category', 'url', 'publish_date', 'desc']
    # exclude = ['appid']

    def save_model(self, request, obj, form, change):
        src = obj.category + obj.application
        appid = hashlib.md5(src.encode('utf8')).hexdigest()
        obj.appid = appid
        super().save_model(request, obj, form, change)
