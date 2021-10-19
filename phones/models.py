from django.db import models


class Phones(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(max_length=120, null=False)
    price = models.FloatField(max_length=100, null=False)
    image = models.ImageField(upload_to='static/image_phone/')
    release_date = models.DateField(null=False)
    lte_exists = models.BooleanField(null=False)
    slug = models.SlugField(null=False)
