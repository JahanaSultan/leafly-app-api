from rest_framework import serializers
from core.models import Teaware


class TeawareSerializer(serializers.ModelSerializer):
    """Serializer for theware object"""
    class Meta:
        model = Teaware
        fields = ['id', 'name', 'price', 'stock_quantity']
        read_only_fields = ['id', 'created_at']


class TeawareDetailSerializer(TeawareSerializer):
    """Serialize a teaware detail"""
    class Meta:
        model=Teaware
        fields = TeawareSerializer.Meta.fields+['description', 'is_available']
