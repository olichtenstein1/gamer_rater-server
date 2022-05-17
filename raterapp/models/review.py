from django.db import models



class Review(models.Model):
    
    description = models.TextField()
    game = models.ForeignKey("Game", on_delete=models.CASCADE, related_name="reviews")
    player = models.ForeignKey("Player", on_delete=models.CASCADE)  