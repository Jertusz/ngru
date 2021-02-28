# Builtins
import logging

# 3rd party
from decouple import Csv
from decouple import config

from .base import *

# Rest Framework
# https://www.django-rest-framework.org/api-guide/settings/

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": ["rest_framework.permissions.AllowAny"],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.TokenAuthentication",
    ],
    "TEST_REQUEST_DEFAULT_FORMAT": "json",
}
