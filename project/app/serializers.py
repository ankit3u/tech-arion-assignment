from rest_framework import serializers
from .models import*

class ProductName(serializers.ModelSerializer):
    class meta:
        model=productMainModel
        fields=['title','description','price']
class ProductList(serializers.ModelSerializer):
    class Meta:
        model=productColourModel
        fields=['product','colour']
class ProductAllList(serializers.ModelSerializer):
    class Meta:
        model=productImageModel
        fields=["product",'image']

