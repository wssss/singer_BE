from django.contrib import admin
from .models import UserAccount, WeChatAccount
# Register your models here.

class UserAccountAdmin(admin.ModelAdmin):
    list_display = ("uuid","phone", "email", "sex")
    


class WeChatAccountAdmin(admin.ModelAdmin):
    list_display = ["uuid", "nickname", "province", "remark"]


admin.site.register(UserAccount, UserAccountAdmin)
admin.site.register(WeChatAccount, WeChatAccountAdmin)



