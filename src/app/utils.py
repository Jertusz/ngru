import requests
import json

API_URL = "https://vpic.nhtsa.dot.gov/api/"


def carExists(manufacturer, model):
    model_list_url = f"vehicles/GetModelsForMake/{manufacturer}?format=json"
    response = requests.get(API_URL+model_list_url)
    models_list = json.loads(response.text)
    models = [row["Model_Name"] for row in models_list["Results"]]
    if model in models:
        return True
    return False

