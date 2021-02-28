from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Manufacturer
from .models import Car
from .models import Rate
from .serializers import CarSerializer
from .utils import carExists
import django.db.utils as dbError
from django.db.models import Avg, Count


class PopularCars(APIView):
    def get(self, request):
        response = []
        cars_sorted_by_rates = Car.objects.all().annotate(rates_number=Count("rate")).order_by('-rates_number')
        for car in cars_sorted_by_rates:
            rates = car.rates_number
            serialized_car = CarSerializer(car)
            partial_response = serialized_car.data
            partial_response["make"] = partial_response["manufacturer"]["name"]
            partial_response.pop("manufacturer")
            partial_response["rates_number"] = rates
            response.append(partial_response)

        return Response(response, status=status.HTTP_200_OK)


class CarDetails(APIView):

    def get(self, request):
        full_response = []
        for car in Car.objects.all():
            serialized_car = CarSerializer(car)
            print(serialized_car)
            response = serialized_car.data
            response["make"] = response["manufacturer"]["name"]
            response["avg_rating"] = Rate.objects.filter(car=car).aggregate(Avg("rating"))
            if response["avg_rating"]["rating__avg"] is None:
                response["avg_rating"] = 0
            else:
                response["avg_rating"] = response["avg_rating"]["rating__avg"]

            response.pop("manufacturer")

            full_response.append(response)
        return Response(full_response, status=status.HTTP_200_OK)

    def post(self, request):

        manufacturer_name = request.data["make"]
        car_name = request.data["model"]

        if carExists(manufacturer_name, car_name):

            try:
                make = Manufacturer.objects.get(name=manufacturer_name)
            except Manufacturer.DoesNotExist:
                make = Manufacturer(name=manufacturer_name)
                make.save()
            try:
                car = Car.objects.get(name=car_name)
                return Response({"message": "Car already exists in database"}, status=status.HTTP_200_OK)
            except Car.DoesNotExist:
                new_car = Car(name=car_name, manufacturer=make)
                new_car.save()
                serialized_car = CarSerializer(new_car)
                return Response(serialized_car.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class DeleteCar(APIView):

    def delete(self, request, pk):

        try:
            car = Car.objects.get(pk=pk)
            car.delete()
            return Response(status=status.HTTP_202_ACCEPTED)
        except Car.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class AddRate(APIView):

    def post(self, request):
        car_id = request.data["car_id"]
        rating = request.data["rating"]

        try:
            car = Car.objects.get(pk=car_id)
            rate = Rate(car=car, rating=rating)
            try:
                rate.save()
            except dbError.IntegrityError:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            return Response(status=status.HTTP_201_CREATED)
        except Car.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
