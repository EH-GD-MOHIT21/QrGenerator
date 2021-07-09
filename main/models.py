from django.db import models

# Create your models here.

class ImageCollector(models.Model):
    image = models.ImageField(upload_to='imgs',null=True,blank=True)

    def __str__(self):
        return str(self.id)
