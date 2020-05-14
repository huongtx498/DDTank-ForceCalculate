from rest_framework import serializers
from .models import Ddtank


class DdtankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ddtank
        fields = ('__all__')
