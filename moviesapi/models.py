from django.db import models

# Create your models here.
class Movies(models.Model):
    title = models.CharField(max_length=40, blank=False, unique=True)
    description = models.TextField(max_length=256, blank=True, null=True)
    ticket_price = models.DecimalField(default=0, max_digits=6, decimal_places=2)
    released = models.DateField(null=True, default=None, blank=True)
    is_released = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='covers/', blank=True)

    def __str__(self):
        return (self.title)
