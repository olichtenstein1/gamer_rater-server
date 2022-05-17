from statistics import mean
from django.db import models



class Game(models.Model):
    
    title = models.CharField(max_length=99)
    description = models.CharField(max_length=99)
    designer = models.CharField(max_length=99)
    year_released = models.DateField()
    number_of_players = models.IntegerField()
    estimated_time_to_play = models.CharField(max_length=99)
    age_recommendation = models.IntegerField()
    player = models.ForeignKey("Player", on_delete=models.CASCADE)
    categories = models.ManyToManyField("Category", through="GameCategories", related_name="games")
    
    
    @property
    def average_rating(self):
        """Average rating calculated attribute for each game"""
        ratings = self.ratings.all()
        average_rating = 0
        if len(ratings) != 0:
            average_rating = mean(ratings)
        
        return average_rating

      # custom property to check if user has reviewed the gme , true or false
      # reference isJoined from level up
      
      
    @property
    def is_rated(self):
        return self.__is_rated

    @is_rated.setter
    def is_rated(self, value):
        self.is_rated = value