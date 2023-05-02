from rest_framework import serializers
from core.models import Tea


class TeaSerializer(serializers.ModelSerializer):
    """Serializer for the tea object"""
    class Meta:
        model = Tea
        fields = ['id', 'name', 'price']
        read_only_fields = ['id', 'created_at']


class TeaDetailSerializer(TeaSerializer):
    """Serialize a tea detail"""
    class Meta:
        model=Tea
        fields = TeaSerializer.Meta.fields+['description', 'is_available']
