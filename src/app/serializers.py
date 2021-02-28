# 3rd party
from rest_framework import serializers

from .models import Manufacturer
from .models import Car
from .models import Rate


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"
