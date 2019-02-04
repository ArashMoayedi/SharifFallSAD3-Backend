from django.contrib import admin
from .models import Item, Rating, PromotionRequest
admin.site.register(Item)
admin.site.register(Rating)
admin.site.register(PromotionRequest)
