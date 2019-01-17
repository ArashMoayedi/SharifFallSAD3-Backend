from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    price = models.IntegerField()
    price_verified = models.BooleanField(default=False)
    item_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.name
