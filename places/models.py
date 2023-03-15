from django.db import models

class Place(models.Model):
    title = models.CharField(max_length=50)
    description_short = models.TextField()
    description_long = models.TextField()
    lng = models.FloatField()
    lat = models.FloatField()
    
    def __str__(self) -> str:
        return self.title
    
class Image(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    image = models.ImageField()
    number = models.SmallIntegerField()

    def __str__(self) -> str:
        return f"{str(self.number)} {self.place.title}"