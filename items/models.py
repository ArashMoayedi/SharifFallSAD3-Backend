from django.db import models
from django.db.models import Avg
from accounts.models import User


class Item(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255, primary_key=True)
    price = models.IntegerField()
    price_verified = models.BooleanField(default=False)
    item_verified = models.BooleanField(default=False)
    item_promoted = models.BooleanField(default=False)


    def __str__(self):
        return self.name

    @property
    def rating(self):
        return Rating.objects.filter(item=self).aggregate(Avg('score'))


rates = zip(range(1, 6), range(1, 6))


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete='CASCADE')
    item = models.ForeignKey(Item, on_delete='CASCADE')
    score = models.IntegerField(choices=rates)
    comment = models.TextField(max_length=2000, null=True)


class PromotionRequest(models.Model):
    item = models.ForeignKey(Item, on_delete='CASCADE')
