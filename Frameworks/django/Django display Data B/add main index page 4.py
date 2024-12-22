# is the landing page when someone visits the root folder of the project
# create a template called main.html:
# {% extends "master.html" %}

# {% block title %}
#   My  Club
# {% endblock %}


# {% block content %}
#   <h1>My  Club</h1>

#   <h3>Players</h3>

#   <p>Check out all our <a href="players/">players</a></p>

# {% endblock %}


# in the view.py add a new that will deal with the main page
# def main(request):
#   template = loader.get_template('main.html')
#   return HttpResponse(template.render())
    
    
# in the urls.py add a new url that will map to the main view
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.main, name='main'),
#     path('players/', views.players, name='players'),
#     path('players/details/<int:id>', views.details, name='details'),
# ]

#           Add a link back to main
# the playes page is missing a link back to main page
#add the link in the all_players.html file in the content block

# {% extends "master.html" %}

# {% block title %}
#   My  Club - List of all players
# {% endblock %}


# {% block content %}

#   <p><a href="/">HOME</a></p>

#   <h1>Players</h1>

#   <ul>
#     {% for x in myplayers %}
#       <li><a href="details/{{ x.id }}">{{ x.firstname }} {{ x.lastname }} {{x.age}}</a></li>
#     {% endfor %}
#   </ul>
# {% endblock %}