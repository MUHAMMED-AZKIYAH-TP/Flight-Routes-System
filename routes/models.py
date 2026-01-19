from django.db import models


class Airport(models.Model):
    code = models.CharField(max_length=10, unique=True)
    
    class Meta:
        ordering = ['code']

    def __str__(self):
        return self.code


class AirportRoute(models.Model):
    airport = models.OneToOneField(
        Airport,
        on_delete=models.CASCADE,
        related_name="airportroute"   
    )
    left = models.ForeignKey(
        Airport, null=True, blank=True,
        on_delete=models.SET_NULL, related_name="left_node"
    )
    right = models.ForeignKey(
        Airport, null=True, blank=True,
        on_delete=models.SET_NULL, related_name="right_node"
    )
    distance_km = models.PositiveIntegerField()
    duration_min = models.PositiveIntegerField()
    
    class Meta:
        ordering = ['airport__code']

    def __str__(self):
        return self.airport.code
