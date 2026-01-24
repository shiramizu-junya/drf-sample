# DRFのResponseクラス。JSONなどの形式でAPIレスポンスを返すために使用します。
from rest_framework.response import Response
from .models import Product, Order
# シリアライザをインポート。モデルのデータをJSON形式に変換する役割。
from .serialize import ProductSerializer, OrderSerializer
# 関数ベースビューをDRFのAPIビューに変換するデコレータ。
from rest_framework.decorators import api_view

# 通常のDjangoビューをDjango REST Frameworkのビューに変換します。
@api_view(['GET', 'POST'])
def product_list(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'POST'])
def order_list(request):
    if request.method == 'GET':
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
