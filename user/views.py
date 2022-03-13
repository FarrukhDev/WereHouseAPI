from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from user.models import Client
from user.serializer import UserSerializer
from rest_framework.filters import SearchFilter

class UserListCreateAPIView(ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = UserSerializer
    filter_backends = [SearchFilter]
    search_fields = ['ism','tel','dokon','manzil','omborxona']

class UserRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = UserSerializer
    filter_backends = [SearchFilter]
    search_fields = ['ism', 'tel', 'dokon', 'manzil', 'omborxona']

