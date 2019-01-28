from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework import viewsets
from .models import User, Company, Store
from .serializers import UserSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def current_user(request):
    """
    Determine the current user by their token, and return their data
    """

    serializer = UserSerializer(request.user)
    return Response(serializer.data)


class UserListView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
