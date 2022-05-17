from django.db import models
from statistics import mean



class Rating(models.Model):
    
    rating = models.IntegerField()
    game = models.ForeignKey("Game", on_delete=models.CASCADE, related_name="ratings")
    player = models.ForeignKey("Player", on_delete=models.CASCADE)
    
    
    