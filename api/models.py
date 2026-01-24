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

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="製品")
    quantity = models.IntegerField(verbose_name="数量")
    order_date = models.DateTimeField(auto_now_add=True, verbose_name="注文日")

    class Meta:
        verbose_name_plural = "注文一覧"

    def __str__(self):
        return f"Order of {self.quantity} x {self.product.name}"
