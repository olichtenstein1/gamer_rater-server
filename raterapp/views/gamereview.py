"""View module for handling requests about game reviews"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.core.exceptions import ValidationError
from raterapp.models.game import Game
from raterapp.models.player import Player

from raterapp.models.review import Review


class ReviewView(ViewSet):
    """Level up game review view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single game review"""
        
        review = Review.objects.get(pk=pk)
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
        
        """Returns:
            Response -- JSON serialized game review
        """
        
    def list(self, request):
        """Handle GET requests to get all game reviews"""
        
        reviews = Review.objects.all()
        
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)

        """Returns:
            Response -- JSON serialized list of game reviews
        """
        
    def create(self, request):
        
        """Handle POST operations

        Returns:
            Response -- JSON serialized game review instance
        """
        player = Player.objects.get(user=request.auth.user)
        serializer = CreateReviewSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(player=player)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        
class ReviewSerializer(serializers.ModelSerializer):
    """JSON serializer for game reviews
    """
    class Meta:
        model = Review
        fields = ('id', 'description', 'player', 'game')
        depth = 1      
        
class CreateReviewSerializer(serializers.ModelSerializer):
    """JSON serializer for creating game reviews
    """
    class Meta:
        model = Review
        fields = ('id', 'description', 'game')