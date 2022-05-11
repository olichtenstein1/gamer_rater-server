"""View module for handling requests about games"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from raterapp.models import Game
from raterapp.models.player import Player
from django.core.exceptions import ValidationError

class GameView(ViewSet):
    """Level up game view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single game"""
        
        game = Game.objects.get(pk=pk)
        serializer = GameSerializer(game)
        return Response(serializer.data)
        
        """Returns:
            Response -- JSON serialized game
        """
    
    
    def list(self, request):
        """Handle GET requests to get all games"""
        
        games = Game.objects.all()
        
        serializer = GameSerializer(games, many=True)
        return Response(serializer.data)

        """Returns:
            Response -- JSON serialized list of games
        """
        
    def create(self, request):
        
        """Handle POST operations

        Returns:
            Response -- JSON serialized game instance
        """
        player = Player.objects.get(user=request.auth.user)
        serializer = CreateGameSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(player=player)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
class GameSerializer(serializers.ModelSerializer):
    """JSON serializer for games
    """
    class Meta:
        model = Game
        fields = ('id', 'title', 'description', 'designer', 'year_released', 'number_of_players', 
                  'estimated_time_to_play', 'age_recommendation', 'player')
        depth = 1      
        
        
class CreateGameSerializer(serializers.ModelSerializer):
    """JSON serializer for creating games
    """
    class Meta:
        model = Game
        fields = ('id', 'title', 'description', 'designer', 'year_released', 'number_of_players', 
                  'estimated_time_to_play', 'age_recommendation')
              