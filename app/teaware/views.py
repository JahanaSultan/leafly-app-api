from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from core.models import Teaware
from teaware import serializers
from core.permissions import AdminOnlyPermission



class TeawareViewSet(viewsets.ModelViewSet):
    """Manage teas in the database"""
    serializer_class = serializers.TeawareDetailSerializer
    queryset = Teaware.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, AdminOnlyPermission)
    
    def get_serializer_class(self):
        """Return serializer class for request"""
        if self.action == 'list':
            return serializers.TeawareSerializer
        
        return self.serializer_class
        