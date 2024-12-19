# to update model means adding more fields to the table created for instance
#from django.db import models
# class Player(models.Model):
#   firstname = models.CharField(max_length=255)
#   lastname = models.CharField(max_length=255)
#   age = models.IntergerField()
#   phone = models.IntegerField()
#   

# we are adding phone and date_joined to the Player model
# since this is a change in the model structure we have to make migrations by using the following command:
"py manage.py makemigrations players"

# the above command will reuslt in a prompt because we are trying to add fields that cannot be nullfied
# py manage.py makemigrations players
# You are trying to add a non-nullable field 'date_joined' to players without a default; we can't do that (the database needs something to populate existing rows).
# Please select a fix:
#  1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
#  2) Quit, and let me add a default in models.py
# Select an option:


# select option 2 open models.py and allow null values for the new fields
# from django.db import models

# class Player(models.Model):
#   firstname = models.CharField(max_length=255)
#   lastname = models.CharField(max_length=255)
#   age = models.IntegerField()
#   phone = models.IntegerField(null=True)
#   date_joined = models.DateField(null=True)

#once done make migrations again
#"py manage.py makemigrations players"
#this will result in the following command
# Migrations for 'players':
#   players\migrations\0002_player_date_joined_player_phone.py
#     - Add field date_joined to player
#     - Add field phone to player

# run "py manage.py migrate" that will result in the following output
# Operations to perform:
#   Apply all migrations: admin, auth, contenttypes, players, sessions
# Running migrations:
#   Applying players.0002_player_date_joined_player_phone... OK

# (myapp) C:\Users\Your Name\myapp\my_club>


#####
# ### insert data to the date_joined and phone value using the python shell
# run the command "python manage.py shell"
# at the >>> add the following info and the [enter]:
# >>> from players.models import Player
# >>> y= player.objects.all()[0]
# >>> y.phone = 748937165
# >>> y.joined_date = '2019-05-10'
# >>> y.save()

# this will info to the first records in the databaase
