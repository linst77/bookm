from django.db import models
from django.urls import reverse
# Create your models here.

class BookM ( models.Model):
    site_name = models.CharField("Site Name", max_length=100)
    site_url = models.URLField("Site URL")

    def __str__(self):
        return "{}".format( self.site_name)

    def get_absolute_url( self):
        return reverse('list', args=[])
        # return reverse( 'detail', args=[str(self.id)])

