from django.db import models

# Create your models here.
class Airport1(models.Model):
    iata= models.CharField(max_length=100)
    icao= models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    location= models.CharField(max_length=100)
    gps= models.CharField(max_length=100)

    def __str__(self):
        return self.iata

class Airport2(models.Model):
    id= models.IntegerField(primary_key=True),
    airport_type=models.CharField(max_length=100)
    airport_name=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    iso_region=models.CharField(max_length=100)
    municipality=models.CharField(max_length=100)
    gps_code=models.CharField(max_length=100)
    iata=models.CharField(max_length=100)
    altitude=models.CharField(max_length=100)
    continent=models.CharField(max_length=100)
    local_code=models.CharField(max_length=100)
    coordinates=models.CharField(max_length=100)

