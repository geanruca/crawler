from django.db import models

class Bus(models.Model):
    title = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    source_url = models.CharField(max_length=255)
    def __str__(self):
        return self.source_url
    def get_images(self):
        return Image.objects.filter(bus=self)

class Image(models.Model):
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    url = models.CharField(max_length=255)
    def __str__(self):
        return self.url