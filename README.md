# Ex02 Django ORM Web Application
## Date: 21.09.2025

## AIM
To develop a Django application to store and retrieve data from a Car Inventory Database using Object Relational Mapping(ORM).

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM

~~~
admin.py

from django.contrib import admin
from .models import CarsRR_DB,CarsRR_DBAdmin
admin.site.register(CarsRR_DB,CarsRR_DBAdmin)

model.py

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

~~~

## OUTPUT:
![alt text](<Screenshot (18).png>)



## RESULT:
Thus the program for creating car inventory database database using ORM hass been executed successfully
