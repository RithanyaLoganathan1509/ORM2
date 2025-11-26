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

