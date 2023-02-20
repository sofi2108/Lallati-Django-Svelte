from django.shortcuts import get_object_or_404
from django.db.models import Count
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail


from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.mixins import RetrieveModelMixin, CreateModelMixin, DestroyModelMixin, UpdateModelMixin
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework import status

from .models import Product, Collection, OrderItem, ShoppingCard, CartItem, Order, OrderItem, Customer
from .serializers import ProductSerializer, ShoppingCardSerializer, CollectionSerializer, CartItemSerializer, AddCartItemSerializer, UpdateItemSerializer, OrderSerializer, customerSerializer
from . import serializers


# Create your views here.
class CaftanViewSet(ModelViewSet):
    queryset = Product.objects.filter(collection=1)
    serializer_class = ProductSerializer

    def destroy(self, request, *args, **kwargs):
        if OrderItem.objects.filter(product_id=kwargs['pk']).count() > 0:
            return Response({'error': 'Product cannot be deleted'}, status=status.HTTP_400_BAD_REQUEST)
        return super().destroy(request, *args, **kwargs)

class AccessoriesViewSet(ModelViewSet):
    queryset = Product.objects.filter(collection=3)
    serializer_class = ProductSerializer

    def destroy(self, request, *args, **kwargs):
        if OrderItem.objects.filter(product_id=kwargs['pk']).count() > 0:
            return Response({'error': 'Product cannot be deleted'}, status=status.HTTP_400_BAD_REQUEST)
        return super().destroy(request, *args, **kwargs) 
    

class CollectionViewSet(ModelViewSet):
    queryset = Collection.objects.annotate(products_count=Count('products')).all()
    serializer_class = CollectionSerializer

    def delete(self, request, pk):
        collection = get_object_or_404(Collection, pk=pk)
        if collection.products.count() > 0:
            return Response({'error': 'Collecion cannot be deleted'},status=status.HTTP_400_BAD_REQUEST)
        collection.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)        


class ShoppingCardViewSet(CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, GenericViewSet):
    queryset = ShoppingCard.objects.prefetch_related('items__product').all()
    serializer_class = ShoppingCardSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        return super().retrieve(request, *args, **kwargs)


class CartItemViewSet(ModelViewSet):
    http_method_names = ['get', 'post', 'patch', 'delete']

    def get_queryset(self):
        return CartItem.objects.filter(cart_id = self.kwargs['cart_pk']).select_related('product')

    def get_serializer_class(self, *args, **kwargs):
        if self.request.method == 'POST':
            return AddCartItemSerializer

        elif self.request.method == 'PATCH':
            return UpdateItemSerializer

        return CartItemSerializer 

    def get_serializer_context(self):
        return {'cart_id':self.kwargs['cart_pk']}

class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class CustomerViewSet(CreateModelMixin, RetrieveModelMixin,UpdateModelMixin, GenericViewSet):
    queryset = Customer.objects.all()
    serializer_class = customerSerializer

@api_view(['POST'])
def send_email(request):
    recipient = request.data['recipient']
    send_mail('Confirm Order', 'Your order has been confirmed', '', [recipient])
    return HttpResponse(recipient,status=status.HTTP_200_OK)

    




            

