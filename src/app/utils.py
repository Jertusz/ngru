# Builtins
import json

# 3rd party
import requests

API_URL = "https://vpic.nhtsa.dot.gov/api/"


def car_exists(manufacturer, model):
    model_list_url = f"vehicles/GetModelsForMake/{manufacturer}?format=json"
    response = requests.get(API_URL + model_list_url)
    models_list = json.loads(response.text)
    models = [row["Model_Name"] for row in models_list["Results"]]
    if model in models:
        return True
    return False


def fix_response(serialized_car):
    partial_response = serialized_car.data
    partial_response["make"] = partial_response["manufacturer"]["name"]
    partial_response.pop("manufacturer")
    return partial_response
