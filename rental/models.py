from django.db import models


# Create your models here.
class Division(models.Model):
    name = models.CharField(null=False, blank=False, max_length=10)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_districts(self):
        return self.district_set.all()


class District(models.Model):
    name = models.CharField(null=False, blank=False, max_length=15)
    division = models.ForeignKey(Division, on_delete=models.SET_NULL, null=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.name
