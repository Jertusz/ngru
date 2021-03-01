# 3rd party
import pytest
from django.test import TestCase
from rest_framework.test import APIClient

# Local
from app.models import Car
from app.models import Manufacturer
from app.models import Rate


@pytest.mark.integration
class TestCarApi(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.manufacturer = Manufacturer(name="Volkswagen")
        cls.manufacturer.save()
        cls.car = Car(manufacturer=cls.manufacturer, name="Golf")
        cls.second_car = Car(manufacturer=cls.manufacturer, name="Passat")
        cls.car.save()
        cls.second_car.save()

        # Adding 3 rates for golf and 2 rates for passat
        for _ in range(3):
            cls.rate = Rate(car=cls.car, rating=4)
            cls.rate.save()
        for _ in range(2):
            cls.rate = Rate(car=cls.second_car, rating=2)
            cls.rate.save()

    def test_popular_car(self):
        api_client = APIClient()
        response = api_client.get("/popular/")

        assert response.status_code == 200
        assert response.data[0]["rates_number"] == 3
        assert response.data[0]["id"] == Car.objects.first().id

    def test_avg_rating(self):
        api_client = APIClient()
        response = api_client.get("/cars/")

        assert response.status_code == 200
        assert response.data[0]["avg_rating"] == 4
        assert response.data[1]["avg_rating"] == 2

    def test_add_existing_car(self):
        api_client = APIClient()
        response = api_client.post("/cars/", {"make": "Honda", "model": "Civic"})

        assert response.status_code == 201
        assert Car.objects.last().name == "Civic"

    def test_add_non_existing_car(self):
        api_client = APIClient()
        response = api_client.post("/cars/", {"make": "Honda", "model": "Passat"})

        assert response.status_code == 500

    def test_add_duplicate_existing_car(self):
        api_client = APIClient()
        response = api_client.post("/cars/", {"make": "Volkswagen", "model": "Golf"})

        assert response.status_code == 200
        assert response.data["message"] == "Car already exists in database"

    def test_delete_car(self):
        api_client = APIClient()
        response = api_client.delete("/cars/2/")

        assert response.status_code == 202
        assert Car.objects.all().count() == 1

    def test_delete_non_existing_car(self):
        api_client = APIClient()
        response = api_client.delete("/cars/20/")

        assert response.status_code == 404

    def test_add_rate(self):
        api_client = APIClient()
        response = api_client.post("/rate/", {"car_id": 1, "rating": 5})

        assert response.status_code == 201
        assert Rate.objects.last().car.id == 1
        assert Rate.objects.last().rating == 5

    def test_add_rate_non_existing_car(self):
        api_client = APIClient()
        response = api_client.post("/rate/", {"car_id": 7, "rating": 5})

        assert response.status_code == 404

    def test_add_rate_out_of_bounds(self):
        api_client = APIClient()
        response = api_client.post("/rate/", {"car_id": 1, "rating": 8})

        assert response.status_code == 400
