from django.db import models

# Create your models here.
class Recepy(models.Model):
    # id = models.Index()
    title = models.CharField(max_length = 50)
    #image = models.ImageField(null = True, blank = True, upload_to = "images/")
    ingredients = models.TextField(max_length=400)
    description = models.TextField()

    author = models.CharField(max_length = 50, default="Author unknown" )
    # id = models.Index()
    # publication = models.DateTimeField(default="2022-")
    tags_choice = (
        ('dish', 'dish'),
    )
    tags = models.TextField(max_length=300, default="dish" """, choice = tags_choice""")
    