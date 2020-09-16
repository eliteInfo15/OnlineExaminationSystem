from rest_framework import serializers
from.models import admin

class AdminSerializers(serializers.ModelSerializers):
    class Meta:
        model=admin
        fields=all

class Categoryserializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields="__all__"

class Centerserializer(serializers.ModelSerializer):
    class Meta:
        model=Center
        fields="__all__"        

class Batchserializer(serializers.ModelSerializer):
    class Meta:
        model=Batch
        fields="__all__"        
        
class Subcategoryserializer(serializers.ModelSerializer):
    class Meta:
        model=Subcategory
        fields="__all__"        
        
