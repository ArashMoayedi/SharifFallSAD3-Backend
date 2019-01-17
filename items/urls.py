from django.urls import include, path, re_path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('items', views.ItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
    re_path(r'^(?P<name>.+)/$', views.ItemListView.as_view()),
]
