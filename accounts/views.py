from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework import viewsets
from .models import User, Company, Store
from .serializers import UserSerializer
from rest_framework import generics


class UserListView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
