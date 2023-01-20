from django.shortcuts import render
from rest_framework import generics
from rest_framework import views
from rest_framework.response import Response
from .serializers import*
from .models import*
# Create your views here.

class ProductListApi(generics.ListCreateAPIView):
    query=productMainModel.objects.all()
    serializer_class=ProductName


