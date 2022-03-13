from rest_framework.serializers import ModelSerializer
from user.models import Client


class UserSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = ['ism','tel','dokon','manzil','omborxona']