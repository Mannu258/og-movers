from django.db import models

# Create your models here.

class contactus(models.Model):
    name = models.CharField(max_length=60)
    mobile = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    price = models.IntegerField()
    from_location = models.TextField()
    to_location = models.TextField()
    date = models.DateField()
    def __str__(self) -> str:
        return self.name    