from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from core.models import Tea
from tea import serializers
from core.permissions import AdminOnlyPermission



class TeaViewSet(viewsets.ModelViewSet):
    """Manage teas in the database"""
    serializer_class = serializers.TeaDetailSerializer
    queryset = Tea.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    
    def get_serializer_class(self):
        """Return serializer class for request"""
        if self.action == 'list':
            return serializers.TeaSerializer
        
        return self.serializer_class
    
        