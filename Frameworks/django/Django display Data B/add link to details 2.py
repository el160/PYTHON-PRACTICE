# this majorly focus on giving more details on the players and then then linked very well
# we create another html file callesd details.html where we will dispaly more on the players
#this is the code for the details.html file:
# <!DOCTYPE html>
# <html>
# <head>
# </head>
# <body>

# <h1>{{ myplayer.firstname }} {{ myplayer.lastname }} {{myplayer.age}}</h1>
  
# <p>Phone: {{ myplayer.phone }}</p>
# <p>Player since: {{ myplayer.joined_date }}</p>

# <p>Back to <a href="/players">Players</a></p>

# </body>
# </html>


           # Add Link to all players Template
# the list in all_membershtml should be clickable, and take you to the details page with the ID of the player you clicked on
#  <!DOCTYPE html>
# <html>
# <head>
# </head>
# <body>

# <h1>Players</h1>
  
# <ul>
#   {% for x in myplayers %}
#     <li><a href="details/{{ x.id }}">{{ x.firstname }} {{ x.lastname }} {{x.age}}</a></li>
#   {% endfor %}
# </ul>

# </body>
# </html>



                  # CREATE A NEW VIEW
# create a view in the views.py file that will render the details.html template with the player 
# from django.http import HttpResponse
# from django.template import loader
# from .models import Player
# def details(request, id):
#   myplayer = Player.objects.get(id=id)
#   template = loader.get_template('details.html')
#   context = {
#     'myplayer': myplayer,
#   }



# the dtails view :
# Gets the id as an argument.
# Uses the id to locate the correct record in the player table.
# loads the details.html template.
# Creates an object containing the player.
# Sends the object to the template.
# Outputs the HTML that is rendered by the template.

#          Add URLs
# in the urls.py file, add a new url pattern that will map to the details view with id as a parameter
#the app urls.py shoul be used:
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.players, name='players'),
#     path('players/details/<int:id>/', views.details, name='details'),
# ]


# finally start the server so as to see if it works