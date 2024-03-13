# mainapp/models.py
from django.db import models

class Game(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='game_images/')
    website = models.CharField(max_length=100, default="")
    def __str__(self):
        return self.title
