from rest_framework import serializers
from.models import admin

class AdminSerializers(serializers.ModelSerializers):
    class Meta:
        model=admin
        fields=all
