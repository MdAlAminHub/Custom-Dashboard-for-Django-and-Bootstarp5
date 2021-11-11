from django.db import models


class Notifications(models.Model):
    devices = models.CharField(max_length=50)
    status = models.CharField(max_length=20)
    title = models.CharField(max_length=20)
    message = models.TextField(max_length=100)
    image_link = models.URLField(max_length=200)

   

    def __str__(self):
       return self.devices



