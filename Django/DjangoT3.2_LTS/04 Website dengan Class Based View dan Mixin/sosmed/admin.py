from django.contrib import admin

from .models import Instagram


# Register your models here.
class InstagramAdmin(admin.ModelAdmin):
    list_display = [
        "nama_depan",
        "nama_belakang",
        "username",
        "content",
    ]


admin.site.register(Instagram, InstagramAdmin)
