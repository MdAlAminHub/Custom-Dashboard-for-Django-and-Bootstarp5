from django.db import models


class Pages(models.Model):
    page_slug = models.CharField(max_length=50, blank=True, null=True)
    page_name_english = models.CharField(max_length=20)
    description_english = models.CharField( max_length=20, blank=True, null=True)
    page_name_bangla = models.CharField(max_length=20)
    description_bangla = models.CharField(max_length=20, blank=True, null=True)


    def __str__(self):
       return self.page_slug
