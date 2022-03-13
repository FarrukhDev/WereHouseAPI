from rest_framework.serializers import ModelSerializer
from ombor.models import Ombor


class OmborSerilizer(ModelSerializer):
    class Meta:
        model = Ombor
        fields = ['ism','tel','ombor','manzil','user']