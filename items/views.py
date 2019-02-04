from rest_framework import viewsets, permissions, serializers
from .models import Item, Rating, PromotionRequest
from .serializers import ItemSerializer, ItemRateSerializer, ItemFullSerializer, RatingSerializer, PromotionRequestSerializer
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


class AllItems(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemFullSerializer


class ItemListView(generics.ListAPIView):
    serializer_class = ItemSerializer

    def get_queryset(self):
        return Item.objects.filter(code=self.kwargs['code'])


class ItemRateView(generics.CreateAPIView):
    serializer_class = ItemRateSerializer

    def perform_create(self, serializer):
        if Rating.objects.filter(user=self.request.user, item=self.request.data['item']).exists():
            ex = Rating.objects.get(user=self.request.user, item=self.request.data['item'])
            ex.score = self.request.data['score']
            ex.comment = self.request.data['comment']
            ex.save(update_fields=["score", "comment"])
        else:
            serializer.save(user=self.request.user)


class PromotionRequestView(generics.CreateAPIView):
    queryset = Item.objects.all()
    serializer_class = PromotionRequestSerializer
    permission_classes = [permissions.AllowAny, ]

    def perform_create(self, serializer):
        serializer.save()


class AllRatings(generics.ListAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
