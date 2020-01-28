from django.contrib import admin
from .models import User
# from .models import  WeChatAccount
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "phone", "email"]


# class WeChatAccountAdmin(admin.ModelAdmin):
#     list_display = ["uuid", "nickname", "province", "remark"]

admin.site.register(User, UserAdmin)
# admin.site.register(WeChatAccount, WeChatAccountAdmin)



