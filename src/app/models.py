from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)

    def __unicode__(self):
        self.name


# This is the model, but decided to rename it because of different meaning in django
class Car(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)


class Rate(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    rating = models.IntegerField()

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(rating__gte=1) & models.Q(rating__lte=5),
                name="Rating is between 1 and 5",
            )
        ]

