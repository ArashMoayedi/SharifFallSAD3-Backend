from rest_framework import viewsets, permissions

from .models import Item
from .serializers import ItemSerializer, ItemRateSerializer
from rest_framework.response import Response
from rest_framework import generics


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all().filter(item_verified=True)
    permission_classes = [permissions.AllowAny, ]
    serializer_class = ItemSerializer

    def create(self, request, *args, **kwargs):
        print("Request data:", request.data)
        serializer = ItemSerializer(data=request.data)
        serializer.is_valid()

        serializer.save()
        return Response({'status': 'Request submitted'})


class ItemListView(generics.ListAPIView):
    serializer_class = ItemSerializer

    def get_queryset(self):
        return Item.objects.filter(name=self.kwargs['name'])


class ItemRateView(generics.ListCreateAPIView):
    serializer_class = ItemRateSerializer

    def get_queryset(self):
        return Item.objects.filter(name=self.kwargs['name'])

