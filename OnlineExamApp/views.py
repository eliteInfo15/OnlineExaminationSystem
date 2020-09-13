from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import admin
from .serializers import AdminSerializers

class Admininfo(viewsets.ModelViewSet):
    queryset =Admin.objects.all()
    serializer_class=AdminSerializer
    
