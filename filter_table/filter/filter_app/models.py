from django.db import models

# Create your models here.

# Name : File name_fake
# type_of : File type_of
# brand_obj : Brand Objective
# brand_sent : Brand sentiment_filter
# seg : Segment

class Data(models.Model):
    name = models.CharField(max_length=25)
    type_of = models.CharField(max_length=4)
    brand_obj = models.CharField(max_length=20)
    brand_sent = models.CharField(max_length=20)
    seg = models.CharField(max_length=3)
    # image path is saved, Thumbnails are saved in static/images
    image = models.CharField(max_length=100)
