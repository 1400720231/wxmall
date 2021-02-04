from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=10, default='', verbose_name="分类")
    index = models.IntegerField(default=0, verbose_name="展示顺序")
    is_delete = models.BooleanField(default=False, verbose_name="是否删除")
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_at = models.DateTimeField(auto_now=True, verbose_name="修改时间")
    level = models.IntegerField(default=1, verbose_name="类目等级")
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.PROTECT,verbose_name="父级类目", related_name="children")

    class Meta:
        verbose_name = "类目表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=10, default='', verbose_name="商品标题")
    font = models.CharField(max_length=256, default='', verbose_name='封面图')
    price = models.DecimalField(max_digits=12, decimal_places=2, default=0.00, verbose_name="价格")
    stock = models.IntegerField(default=0, verbose_name="库存")
    is_valid = models.BooleanField(default=False, verbose_name="下架")
    is_delete = models.BooleanField(default=False, verbose_name="删除")
    sold_times = models.IntegerField(default=0, verbose_name="售出总数")
    comment_times = models.IntegerField(default=0, verbose_name="评论总数")
    desc = models.TextField(verbose_name="详情")
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_at = models.DateTimeField(auto_now=True, verbose_name="修改时间")

    class Meta:
        verbose_name = "商品表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Image(models.Model):
    product = models.ForeignKey(Product, null=True, blank=True, related_name='images', on_delete=models.PROTECT,
                                verbose_name="商品")
    image = models.CharField(max_length=256, default='', verbose_name='商品轮播图')
    index = models.IntegerField(default=0, verbose_name="轮播顺序")
    is_delete = models.BooleanField(default=False, verbose_name="是否删除")
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_at = models.DateTimeField(auto_now=True, verbose_name="修改时间")

    class Meta:
        verbose_name = "商品轮播图"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.image


class Banner(models.Model):
    product = models.ForeignKey(Product, null=True, blank=True, related_name='banners', on_delete=models.PROTECT,
                                verbose_name="轮播商品")
    index = models.IntegerField(default=0, verbose_name="轮播顺序")
    is_delete = models.BooleanField(default=False, verbose_name="是否删除")
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_at = models.DateTimeField(auto_now=True, verbose_name="修改时间")

    class Meta:
        verbose_name = "商品轮播图"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.product.title
