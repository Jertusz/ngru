import pytest
import requests
from django.test import TestCase

from app.utils import car_exists
from app.utils import fix_response
from app.models import Car
from app.models import Manufacturer
from app.serializers import CarSerializer


@pytest.mark.unit
class TestUtils(TestCase):

    def test_check_for_existing_car_in_external_api(self):
        manufacturer = "Volkswagen"
        model = "Golf"

        result = car_exists(manufacturer, model)

        assert result is True

    def test_check_for_non_existing_car_in_external_api(self):
        manufacturer = "Volkswagen"
        model = "NonExisting"

        result = car_exists(manufacturer, model)

        assert result is False

    def test_response_fix(self):
        manufacturer = Manufacturer(name="Volkswagen")
        car = Car(manufacturer=manufacturer, name="Golf")
        serialized_car = CarSerializer(car)
        fixed_response = fix_response(serialized_car)

        assert "manufacturer" not in fixed_response.keys()
        assert fixed_response["make"] == "Volkswagen"

