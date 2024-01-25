from django.db import models

# Create your models here.
class Travelpackage(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    price_per_person = models.DecimalField(max_digits=10, decimal_places=2)
    deposit_per_person = models.DecimalField(max_digits=10, decimal_places=2)
    includes = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    special_notes = models.TextField(blank=True, null=True)
    

    def __str__(self):
        return self.name
