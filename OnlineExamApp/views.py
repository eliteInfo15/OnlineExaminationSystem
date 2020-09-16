from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from.models import Admin,Category,Batch,Center,Subcategory
from.serializers import AdminSerializers,Categoryserializer,Batchserializer,Centerserializer,Subcategoryserializer

class Admininfo(viewsets.ModelViewSet):
    queryset =Admin.objects.all()
    serializer_class=AdminSerializer
    

class Categoryview(viewsets.ModelViewSet):
    queryset=Category.objects.all()
    serializer_class=Categoryserializer
    
class Centerview(viewsets.ModelViewSet):
    queryset=Center.objects.all()
    serializer_class=Centerserializer
    
class Batchview(viewsets.ModelViewSet):
    queryset=Batch.objects.all()
    serializer_class=Batchserializer        

class Subcategoryview(viewsets.ModelViewSet):
    queryset=Subcategory.objects.all()
    serializer_class=Subcategoryserializer      
    
