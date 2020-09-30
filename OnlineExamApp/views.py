from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from.models import Admin,Batch,Center,Category,Subcategory
from.serializers import Adminserializer,Batchserializer,Centerserializer,Categoryserializer,Subcategoryserializer
    
class Adminview(viewsets.ModelViewSet):
    queryset=Admin.objects.all()
    serializer_class=Adminserializer

# Create your views here.
class Adminbyname(APIView):
    def get(self,request,name):
        Admins=Admin.objects.get(username=name)
        serializer=Admin
        return Response(serializer.data)
      
class Categoryview(viewsets.ModelViewSet):
    queryset=Category.objects.all()
    serializer_class=Categoryserializer
    
class Categorybyname(APIView):
    def get(self,request,name):
        categories=Category.objects.get(category_name=name)
        serializer=Categoryserializer(categories)
        return Response(serializer.data)
      
class Centerview(viewsets.ModelViewSet):
    queryset=Center.objects.all()
    serializer_class=Centerserializer
    
class Centername(APIView):
    def get(sef,request,center_name):
        center1=Center.objects.get(center_name=center_name)
        serializer=Centerserializer(center1)
        return Response(serializer.data) 
        
class Batchview(viewsets.ModelViewSet):
    queryset=Batch.objects.all()
    serializer_class=Batchserializer     
    
class Batchtime(APIView):
    def get(self,request,batch_time):
        batch1=Batch.objects.get(batch_time=batch_time)
        serializer=Batchserializer(batch1)
        return Response(serializer.data)  
    
class Subcategoryview(viewsets.ModelViewset):
    queryset=Subcategory.objects.all()
    serializer_class=Subcategoryserializer
    
class Subcategoryname(APIView):
    def get(self,request,subcategory_name):
        subcategory1=Subcategory.objects.get(subcategory_name=subcategory_name)
        serializer=Subcategoryserializer(subcategory1)
        return Response(serializer.data) 
