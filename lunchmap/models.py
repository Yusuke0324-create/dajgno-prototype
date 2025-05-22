from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Shop(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
    )
    image = models.ImageField(upload_to='shop_images/', null = True, blank = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

class Blog(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)  # 関連店舗
    title = models.CharField(max_length=200)
    content = RichTextUploadingField()  # 画像挿入が可能なリッチテキストエリア
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # 誰が投稿したか
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title