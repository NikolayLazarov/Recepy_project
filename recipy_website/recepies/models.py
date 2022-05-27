from django.db import models

# Create your models here.
class Recepy(models.Model):
    title = models.CharField(max_length = 50)
    ingredients = models.TextField(max_length=400)
    description = models.TextField()
    # author = models(max_length = 100)
    
    