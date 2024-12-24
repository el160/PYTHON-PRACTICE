#to incluse a player model in the admin interface we have to django that the model should be visible in the admin interface
# this is done in the admin.py folder located in the app's folder
# in the file add code to make Player model visible in admin page
# from django.contrib import admin
# from .models import Player

# # Register your models here.
# admin.site.register(Player)
# this will make the Player model visible in the admin page
# click players and you will see alist of players available

# in order to have a better display of the players in the admin page we can use django's built-in admin interface
#change setings in the models.py or admin.py file