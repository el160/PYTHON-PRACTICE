#when we display a model as a list django displays easch record as string representation of the record object
# to change into a more readable format we use two methods:
#1. Change the string representation function, __str__() of the Player Model
# go the models.py folder and define the __str__() function
#from django.db import models

# class Player(models.Model):
#   firstname = models.CharField(max_length=255)
#   lastname = models.CharField(max_length=255)
#   age = models.IntegerField()
#   phone = models.IntegerField(null=True)
#   Date_joined = models.DateField(null=True)

#   def __str__(self):
#     return f"{self.firstname} {self.lastname} {self.age}"

#2.Set the list_details property of the Member Model(reccomended)
# we can control what to display by specifying in list_dispaly property in the admin.py file
# we create PlayerAdmin() class and specify list_display tuple:
# always add PlayerAdmin as an argument

# from django.contrib import admin
# from .models import Player

# # Register your models here.

# class PlayerAdmin(admin.ModelAdmin):
#   list_display = ("firstname", "lastname", "date_joined",)
  
# admin.site.register(Player, PlayerAdmin)

