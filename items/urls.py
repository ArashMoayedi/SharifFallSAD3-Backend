from django.urls import include, path, re_path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('items', views.ItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('all/', views.AllItems.as_view()),
    path('ratings/', views.AllRatings.as_view()),
    re_path(r'^search/(?P<code>.+)/$', views.ItemListView.as_view()),
    path('rate/', views.ItemRateView.as_view()),
    path('promote/', views.PromotionRequestView.as_view())
]
