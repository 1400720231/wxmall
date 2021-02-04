from django.db import models
from goods.models import Product
from django.contrib.auth import  get_user_model
User = get_user_model()
# Create your models here.
class Order(models.Model):
    STATUS_CHIOCE = (
        (1, '待付款'),
        (2, "已付款"),
        (3, "已关闭")
    )
    user = models.ForeignKey(User, null=True, blank=True, related_name='orders', verbose_name="用户",
                             on_delete=models.PROTECT)
    product = models.ForeignKey(Product, null=True, blank=True, related_name='orders', verbose_name="商品",
                                on_delete=models.PROTECT)
    number = models.IntegerField(default=0, verbose_name="数量")
    price = models.DecimalField(max_digits=12, decimal_places=2, default=0.00, verbose_name="总价")
    status = models.IntegerField(choices=STATUS_CHIOCE, default=1, verbose_name="订单状态")
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_at = models.DateTimeField(auto_now=True, verbose_name="修改时间")

    class Meta:
        verbose_name = "商品轮播图"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.product


class OrderDetail(models.Model):
    STATUS_CHIOCE = (
        (1, '待付款'),
        (2, '待发货'),
        (3, "待确认"),
        (4, "待评价"),
        (5, "已完成"),
        (6, "已关闭")
    )
    user = models.ForeignKey(User, null=True, blank=True, related_name='order_details', verbose_name="用户",
                             on_delete=models.PROTECT)
    order = models.ForeignKey(Order, null=True, blank=True, related_name='order_details', verbose_name="订单",
                              on_delete=models.PROTECT)
    number = models.IntegerField(default=0, verbose_name="数量")
    price = models.DecimalField(max_digits=12, decimal_places=2, default=0.00, verbose_name="总价")
    status = models.IntegerField(choices=STATUS_CHIOCE, default=1, verbose_name="订单状态")
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_at = models.DateTimeField(auto_now=True, verbose_name="修改时间")

    class Meta:
        verbose_name = "商品轮播图"
        verbose_name_plural = verbose_name


class Cart(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, related_name='carts', verbose_name="用户",
                             on_delete=models.PROTECT)
    product = models.ForeignKey(Product, null=True, blank=True, related_name='carts', verbose_name="商品",
                                on_delete=models.PROTECT)
    number = models.IntegerField(default=0, verbose_name="数量")
    is_delete = models.BooleanField(default=False, verbose_name="是否删除")
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_at = models.DateTimeField(auto_now=True, verbose_name="修改时间")

    class Meta:
        verbose_name = "商品轮播图"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.product


class Comment(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, related_name='images', verbose_name="用户",
                             on_delete=models.PROTECT)
    product = models.ForeignKey(Product, null=True, blank=True, related_name='products', verbose_name="商品",
                                on_delete=models.PROTECT)
    order = models.ForeignKey(Order, null=True, blank=True, related_name='orders', verbose_name="订单",
                              on_delete=models.PROTECT)
    comment = models.CharField(max_length=500, default='', verbose_name="评价内容")
    is_delete = models.BooleanField(default=False, verbose_name="是否删除")
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_at = models.DateTimeField(auto_now=True, verbose_name="修改时间")

    class Meta:
        verbose_name = "评论"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user
