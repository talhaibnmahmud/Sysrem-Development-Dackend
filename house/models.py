from django.core.validators import MaxValueValidator
from django.db import models

from rental.models import Division, District

HOUSE_TYPE = [
    ('Apartment', 'Apartment'),
    ('Duplex', 'Duplex'),
    ('Triplex', 'Triplex'),
]


# Create your models here.
class House(models.Model):
    title = models.CharField(max_length=100)
    address = models.CharField(max_length=100, default='')
    division = models.ForeignKey(Division, on_delete=models.SET_NULL, null=True)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True)
    price = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(10000000)])
    type = models.CharField(max_length=15, choices=HOUSE_TYPE, default=HOUSE_TYPE[0])
    area = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(100000)])
    beds = models.PositiveSmallIntegerField(default=0, validators=[MaxValueValidator(15)])
    baths = models.PositiveSmallIntegerField(default=0, validators=[MaxValueValidator(10)])
    kitchen = models.PositiveSmallIntegerField(default=0, validators=[MaxValueValidator(5)])
    drawing = models.PositiveSmallIntegerField(default=0, validators=[MaxValueValidator(5)])
    dining = models.PositiveSmallIntegerField(default=0, validators=[MaxValueValidator(5)])
    parking_space = models.PositiveSmallIntegerField(default=0, blank=True)
    elevators = models.PositiveSmallIntegerField(default=0, blank=True)
    balcony = models.BooleanField(default=False)
    electricity_backup = models.BooleanField(default=False)
    service_elevator = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    description = models.TextField(max_length=300, blank=True)

    def __str__(self):
        if self.title is not None:
            return str(self.title)
