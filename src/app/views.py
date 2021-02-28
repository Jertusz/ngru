from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Manufacturer
from .models import Car
from .models import Rate
from .serializers import CarSerializer
from .utils import carExists
import django.db.utils as dbError


class AddCar(APIView):
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
