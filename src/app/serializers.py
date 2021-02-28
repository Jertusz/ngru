# 3rd party
from rest_framework import serializers

from .models import Car
from .models import Manufacturer


class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = [
            "name",
        ]


class CarSerializer(serializers.ModelSerializer):
    manufacturer = ManufacturerSerializer()

    class Meta:
        model = Car
        fields = "__all__"
