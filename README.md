# Ex01 Django ORM Web Application
## Date: 26.11.2025

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
Execute Django admin and create details for 5 Car 

## PROGRAM
```
admin.py

from django.contrib import admin
from .models import CarInventory,CarInventoryAdmin
admin.site.register(CarInventory,CarInventoryAdmin)

models.py

from django.db import models
from django.contrib import admin
class CarInventory (models.Model):
    Car_Company=models.CharField(max_length=20)
    Car_Model=models.CharField(max_length=20)
    Car_Colour=models.CharField(max_length=20)
    Fuel_Type=models.CharField(max_length=20)
    Car_Price=models.DecimalField(max_digits=20,decimal_places=2)

class CarInventoryAdmin(admin.ModelAdmin):
    list_display=('Car_Company','Car_Model','Car_Colour','Fuel_Type','Car_Price')

```
## OUTPUT
![alt text](<Screenshot 2025-11-26 083832.png>)

## RESULT
Thus the program for creating car inventory database database using ORM hass been executed successfully
