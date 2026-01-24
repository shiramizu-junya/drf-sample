from rest_framework import serializers
from .models import Product, Order

class ProductSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
          max_length=100,
          error_messages={
              'required': '商品名は必須です',
              'blank': '商品名を空にはできません',
              'max_length': '商品名は100文字以内で入力してください',
          }
      )

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'product', 'quantity', 'order_date']
