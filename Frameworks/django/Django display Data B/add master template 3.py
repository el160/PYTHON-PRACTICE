#  a master template is a parent template that can include all the information in all html templated(master.html)
# below is a master.html file
#the block inside title and body are placeholders telling django to replace the block content from other sources
# <!DOCTYPE html>
# <html>
# <head>
#   <title>{% block title %}{% endblock %}</title>
# </head>
# <body>

# {% block content %}
# {% endblock %}

# </body>
# </html>

               # Modfy Templates
# the all_players.html amd details.html can use the master template
# this is achieved by including master template with {%extentds%} tag and inserting a title and content blocks
#in all_players.html:

# {% extends "master.html" %}

# {% block title %}
#   My  Club - List of all players
# {% endblock %}


# {% block content %}
#   <h1>Players</h1>
  
#   <ul>
#     {% for x in myplayers %}
#       <li><a href="details/{{ x.id }}">{{ x.firstname }} {{ x.lastname }} {{x.age}}</a></li>
#     {% endfor %}
#   </ul>
# {% endblock %}


# in details.html file
# {% extends "master.html" %}

# {% block title %}
#   Details about {{ myplayer.firstname }} {{ myplayer.lastname }} {{myplayer.age}}
# {% endblock %}


# {% block content %}
#   <h1>{{ myplayer.firstname }} {{ myplayer.lastname }} {{myplayer.age}}</h1>
  
#   <p>Phone {{ myplayer.phone }}</p>
#   <p>Member since: {{ myplayer.joined_date }}</p>
  
#   <p>Back to <a href="/players">Players</a></p>
  
# {% endblock %}