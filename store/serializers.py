from rest_framework import serializers
from .models import Store, Product, DeliveryPerson, OrderHistory
from django.conf import settings
from django.contrib.auth.models import User

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        # aqui se consultan todos los campos en la tabla de store
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields='__all__'

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        # aqui se consultan todos los campos en la tabla de productos
        fields = '__all__'

class DeliveryPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryPerson
        # aqui se consultan todos los campos en la tabla de delivery person
        fields = '__all__'

class OrderHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderHistory
        # aqui se consultan todos los campos en la tabla de delivery ordenes
        fields = '__all__'


