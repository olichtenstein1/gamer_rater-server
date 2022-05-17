from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from raterapp.models import Category
from django.core.exceptions import ValidationError

class CategoryView(ViewSet):
    """Level up game view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single category"""
        
        category = Category.objects.get(pk=pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)
        
        """Returns:
            Response -- JSON serialized category
        """
    
    
    def list(self, request):
        """Handle GET requests to get all categories"""
        
        categories = Category.objects.all()
        
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

        """Returns:
            Response -- JSON serialized list of categories
        """
        
class CategorySerializer(serializers.ModelSerializer):
    """JSON serializer for categories
    """
    class Meta:
        model = Category
        fields = ('id', 'label')