# 3rd party
from django.contrib import admin
from .models import Manufacturer
from .models import Car
from .models import Rate

admin.site.register(Manufacturer)
admin.site.register(Car)
admin.site.register(Rate)
