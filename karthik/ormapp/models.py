from django.db import models
from django.contrib import admin
class CarsRR_DB(models.Model):
      car_model=models.CharField(max_length=10)
      series=models.CharField()
      color=models.CharField(max_length=8)
      price=models.IntegerField(primary_key=True)
      fancy_number=models.IntegerField()
class CarsRR_DBAdmin(admin.ModelAdmin):
      list_display=["car_model","series","color","price","fancy_number"]