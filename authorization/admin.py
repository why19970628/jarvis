from django.contrib import admin

# Register your models here.
from .models import User
# Register your models here.

# admin.site.register(User)


@admin.register(User)
class AuthorizationUserAdmin(admin.ModelAdmin):
    exclude = ['open_id']