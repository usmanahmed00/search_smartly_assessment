from django.db import models


class PointOfInterest(models.Model):
    internal_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    external_id = models.CharField(max_length=50)
    category = models.CharField(max_length=100)
    avg_rating = models.FloatField(default=0.0)

    def __str__(self):
        return self.name
