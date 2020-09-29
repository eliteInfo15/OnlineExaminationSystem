from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from.models import Admin
from.serializers import Adminserializer

class Admininfo(viewsets.ModelViewSet):
    queryset =Admin.objects.all()
    serializer_class=AdminSerializer
    
    
class Adminbyname(APIView):
    def get(self,request,name):
        Admins=Admin.objects.get(username=name)
        serializer=Admin
        return Response(serializer.data)
      
