from django.db import models

# Create your models here.
class Recepy(models.Model):
    # id = models.Index()
    title = models.CharField(max_length = 50)
    #image = models.ImageField(null = True, blank = True, upload_to = "images/")
    ingredients = models.TextField(max_length=400)
    description = models.TextField()

    # author = models(max_length = 100)
    
    