from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="製品名")
    description = models.TextField(verbose_name="製品説明")
    price = models.IntegerField(max_length=100, verbose_name="価格")

    class Meta:
        verbose_name_plural = "製品一覧"

    def __str__(self):
        return self.name
