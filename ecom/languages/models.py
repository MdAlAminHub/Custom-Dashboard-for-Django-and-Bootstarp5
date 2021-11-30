from django.db import models


class Languages(models.Model):
    name=models.CharField(max_length=50)
    code=models.CharField(max_length=20)
    icon = models.ImageField(
        upload_to='static/assets/images/language_icons', blank=True, null=True)
    directory = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
       return self.name
