
from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class ApiUser(AbstractUser):
    ...


class Warehouse(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.id}: {self.name}"


class Product(models.Model):
    name = models.CharField(max_length=300)
    warehouse = models.ForeignKey(Warehouse, related_name="id", on_delete=models.CASCADE)
    count = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name.name}. warehouse: {self.warehouse}. count {self.count}"

