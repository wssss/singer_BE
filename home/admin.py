from django.contrib import admin

# Register your models here.
from .models import  Banner



class BannerAdmin(admin.ModelAdmin):
    list_display = ["image", "name", "orders", "link"]


admin.site.register(Banner, BannerAdmin)

