from django.db import models



class Picture(models.Model):
    
    image = models.CharField(max_length=99)
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    player = models.ForeignKey("Player", on_delete=models.CASCADE)  