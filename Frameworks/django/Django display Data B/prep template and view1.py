# majorly used to display data in the webpage
# navigate to the templates folder in the app's (players) folder and create a htmlfile all_players.html
# the html file should have the following information
# <!DOCTYPE html>
# <html>
# <head>
# </head>
# <body>

# <h1>Playerss</h1>
  
# <ul>
#   {% for x in myplayers %}
#     <li>{{ x.firstname }} {{ x.lastname }} {{ x.age }}</li>
#   {% endfor %}
# </ul>

# </body>
# </html>

# {% %} are django tags that are used to display data in the webpage

# modify View
# here we make the model data to be available in the template
# in the views.py we have the Player model and here is how we send it to the template
# from django.http import HttpResponse
# from django.template import loader
# from .models import Player

# def players(request):
#   myplayers = Player.objects.all().values()
#   template = loader.get_template('all_players.html')
#   context = {
#     'myplayers': myplayers,
#   }
#   return HttpResponse(template.render(context, request))
#   # return HttpResponse(myplayers) # this will return the data in the json format


# the players view.py does:
# Creates a myplayers object with all the values of the Player model.
# Loads the all_players.html template.
# Creates an object containing the myplayers object.
# Sends the object to the template.
# Outputs the HTML that is rendered by the template.


# start the server so that youcan see the results on the webpage