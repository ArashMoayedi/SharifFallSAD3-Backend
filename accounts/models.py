from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    fullName = models.CharField(max_length=24, null=True)
    owns_store = models.BooleanField('owns_store', default=False)
    owns_company = models.BooleanField('owns_company', default=False)

    def __str__(self):
        return self.username


class Store(models.Model):
    owner = models.ManyToManyField(User)
    name = models.CharField(max_length=256)
    location = models.CharField(max_length=512)

    def __str__(self):
        return self.name


class Company(models.Model):
    owner = models.ManyToManyField(User)
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=512)

    def __str__(self):
        return self.name
