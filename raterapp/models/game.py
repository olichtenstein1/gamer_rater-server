from django.db import models



class Game(models.Model):
    
    title = models.CharField(max_length=99)
    description = models.CharField(max_length=99)
    designer = models.CharField(max_length=99)
    year_released = models.DateField()
    number_of_players = models.IntegerField()
    estimated_time_to_play = models.DateField()
    age_recommendation = models.IntegerField()
    player = models.ForeignKey("Player", on_delete=models.CASCADE)
    
    
    