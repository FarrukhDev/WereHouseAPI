from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateDestroyAPIView,ListCreateAPIView
from ombor.models import Ombor
from ombor.serializer import OmborSerilizer
from rest_framework.filters import SearchFilter

class OmborListCreateAPIView(ListCreateAPIView):
    queryset = Ombor.objects.all()
    serializer_class = OmborSerilizer
    filter_backends = [SearchFilter]
    search_fields = ['ism','tel','ombor','manzil','user']

class OmborRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Ombor.objects.all()
    serializer_class = OmborSerilizer
    filter_backends = [SearchFilter]
    search_fields = ['ism','tel','ombor','manzil','user']
