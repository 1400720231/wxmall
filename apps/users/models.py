from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    """
    用户表
    """
    openid = models.CharField(max_length=128, default='', verbose_name="微信openid")
    avatar = models.CharField(max_length=256, default='', verbose_name="微信头像")
    gender = models.CharField(max_length=10, default="女", verbose_name="性别")
    phone = models.CharField(max_length=20, default="", verbose_name="手机号")
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_at = models.DateTimeField(auto_now=True, verbose_name="修改时间")

    class Meta:
        verbose_name = "用户表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class Address(models.Model):
    user = models.ForeignKey(UserProfile, null=True, blank=True, related_name='address', on_delete=models.PROTECT,
                             verbose_name="用户")
    name = models.CharField(max_length=50, verbose_name="收货人姓名")
    phone = models.CharField(max_length=50, default='', verbose_name="收货人电话")
    block = models.CharField(max_length=256, default='', verbose_name="收货人地址")
    is_default = models.BooleanField(default=False, verbose_name="是否为默认地址")
    is_delete = models.BooleanField(default=False, verbose_name="是否删除")
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_at = models.DateTimeField(auto_now=True, verbose_name="修改时间")

    class Meta:
        verbose_name = "收货地址"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user
