from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.core.exceptions import ValidationError
from raterapp.models.game import Game
from raterapp.models.player import Player

from raterapp.models.rating import Rating





class RatingView(ViewSet):
    """Level up game rating view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single game rating"""
        
        rating = Rating.objects.get(pk=pk)
        serializer = RatingSerializer(rating)
        return Response(serializer.data)
        
        """Returns:
            Response -- JSON serialized game rating
        """
        
    def list(self, request):
        """Handle GET requests to get all game ratings"""
        
        ratings = Rating.objects.all()
        
        serializer = RatingSerializer(ratings, many=True)
        return Response(serializer.data)

        """Returns:
            Response -- JSON serialized list of game ratings
        """
        
    def create(self, request):
        
        """Handle POST operations

        Returns:
            Response -- JSON serialized game rating instance
        """
        player = Player.objects.get(user=request.auth.user)
        serializer = CreateRatingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(player=player)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
class RatingSerializer(serializers.ModelSerializer):
    """JSON serializer for game ratings
    """
    class Meta:
        model = Rating
        fields = ('id', 'rating', 'player', 'game')
        depth = 1      
        
class CreateRatingSerializer(serializers.ModelSerializer):
    """JSON serializer for creating game ratings
    """
    class Meta:
        model = Rating
        fields = ('id', 'rating', 'game')
        