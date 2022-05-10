from django.db import models



class Review(models.Model):
    
    description = models.TextField()
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    player = models.ForeignKey("Player", on_delete=models.CASCADE)  