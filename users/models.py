from django.db import models
import uuid
from django.contrib.auth import get_user_model
from django.contrib.postgres import fields as pg_fields
from django.db import transaction
from django.conf import settings
# Create your models here.

UserModel = get_user_model()

class WeChatAccount(models.Model):
    """微信账户信息
    """
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    create_time = models.DateField(verbose_name="创建时间", auto_now_add=True)

    user = models.OneToOneField(
        UserModel,
        unique=True,
        null=True,
        on_delete=models.PROTECT,
        verbose_name="对方验证账号",
        related_name="wechat"
    )

    openid = models.CharField(verbose_name="微信账户 OpenID", max_length=32, blank=True)
    unionid = models.CharField(verbose_name="微信账户 UnionID", max_length=32, blank=True)

    groupid = models.IntegerField(
        verbose_name="性别", choices=((0,'未知'),(1,'男'), (2, '女')), default=0
    )
    nickname = models.CharField(verbose_name="微信昵称", max_length=128, blank=True, default="")

    city = models.CharField(verbose_name="市", blank=True, max_length=16)
    province = models.CharField(verbose_name="省", blank=True, max_length=16)
    subscribe_time = models.DateTimeField(verbose_name="订阅时间", auto_now=False)
    headimgurl = models.CharField(verbose_name="头像 URL" , blank=True, max_length=25)
    language = models.CharField(verbose_name="语言", blank=True, max_length=16)
    remark = models.TextField(verbose_name="备注", blank=True)

    class Meta:
        verbose_name = verbose_name_plural = "微信账户"

    def __str__(self):
        return self.nickname or self.unionid or self.openid


class UserAccount(models.Model):
    """ 账户信息"""
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    create_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    update_time = models.DateTimeField(verbose_name="更新时间", auto_now=True)
    user = models.OneToOneField(
        UserModel,
        unique=True,
        on_delete=models.PROTECT,
        verbose_name="对应验证账号",
        related_name="account",
    )
    role = models.CharField(
        verbose_name="用户角色",
        max_length=16,
        default="normal",
        blank=True,
    )
    # 网站用户信息
    phone = models.CharField(verbose_name="手机号", max_length=11, unique=True)
    email = models.EmailField(verbose_name="邮箱地址", blank=True)
    nickname = models.CharField(
        verbose_name="昵称", max_length=32, blank=True, default=""
    )
    sex = models.IntegerField(
        verbose_name="性别", choices=((0,'未知'),(1,'男'), (2, '女')), default=0
    )
    avatar = models.ImageField(
        verbose_name="头像",
        upload_to='images',
        blank=True,
        null=True,
    )
    avatar_url = models.CharField(verbose_name="头像URL", max_length=255, blank=True)
    # 账户注册来源
    registration_source = models.IntegerField(
        verbose_name="注册来源",
        default=0,
    )

    class Meta:
        verbose_name = verbose_name_plural = "账户信息"

    def __str__(self):
        return self.phone

    @property
    def get_avatar_url_display(self):
        if self.avatar_url:
            return f"{settings.ALI_OSS_BASE_URL}{self.avatar_url}"
        return ""
