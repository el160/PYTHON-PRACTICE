# in the project we want to add a stylesheet(mystyles.css) and put in in mystatic files folder
#my_club
    # manage.py
    # my_club/
    # members/
    # mystaticfiles/
    #     mystyles.css
    
# # open the css file and add the following code
# body {
#   background-color: yellow;
# }


#    Modify the Master Template

# include the mystyless.css file in the master template
# % load static %}
# <!DOCTYPE html>
# <html>
# <head>
#   <title>{% block title %}{% endblock %}</title>
#   <link rel="stylesheet" href="{% static 'mystyles.css' %}">  
# </head>
# <body>

# {% block content %}
# {% endblock %}

# </body>
# </html>


# make sure settings.py file contians STATICFILES_DIRS list with refernce to the mystaticfiles folder on root directory
#and you have specified a STATICFILES_ROOT folder
# STATIC_ROOT = BASE_DIR / 'productionfiles'

# STATIC_URL = 'static/'

# #Add this in your settings.py file:
# STATICFILES_DIRS = [
#     BASE_DIR / 'mystaticfiles'
# ]



# evertime you make achange collect the static files uising the collectstatic command


# to add more appealing content in mystyles.css file add the following code

# @import url('https://fonts.googleapis.com/css2?family=Source+Sans+Pro:wght@400;600&display=swap');
# body {
#   margin:0;
#   font: 600 18px 'Source Sans Pro', sans-serif;
#   letter-spacing: 0.64px;
#   color: #585d74;
# }
# .topnav {
#   background-color:#375BDC;
#   color:#ffffff;
#   padding:10px;
# }
# .topnav a:link, .topnav a:visited {
#   text-decoration: none;
#   color: #ffffff; 
# }
# .topnav a:hover, .topnav a:active {
#   text-decoration: underline;
# }
# .mycard {
#   background-color: #f1f1f1;
#   background-image: linear-gradient(to bottom, #375BDC, #4D70EF); 
#   background-size: 100% 120px;
#   background-repeat: no-repeat;
#   margin: 40px auto;
#   width: 350px;
#   border-radius: 5px;
#   box-shadow: 0 5px 7px -1px rgba(51, 51, 51, 0.23); 
#   padding: 20px;
# }
# .mycard h1 {
#   text-align: center;
#   color:#ffffff;
#   margin:20px 0 60px 0;
# }
# ul {
#   list-style-type: none;
#   padding: 0;
#   margin: 0;
# }
# li {
#   background-color: #ffffff;
#   background-image: linear-gradient(to right, #375BDC, #4D70EF); 
#   background-size: 50px 60px;
#   background-repeat: no-repeat;
#   cursor: pointer;
#   transition: transform .25s;
#   border-radius: 5px;
#   box-shadow: 0 5px 7px -1px rgba(51, 51, 51, 0.23);
#   padding: 15px;
#   padding-left: 70px;
#   margin-top: 5px;
# }
# li:hover {
#   transform: scale(1.1);
# }
# a:link, a:visited {
#   color: #375BDC; 
# }
# .main, .main h1 {
#   text-align:center;
#   color:#375BDC;
# }




#            modify the templates

# 1. master.html
#we want all pages to have top navigation bartherfore we insert the top navigation ino master.html
# {% load static %}
# <!DOCTYPE html>
# <html>
# <head>
#   <link rel="stylesheet" href="{% static 'mystyles.css' %}">
#   <title>{% block title %}{% endblock %}</title>
# </head>
# <body>

# <div class="topnav">
#   <a href="/">HOME</a> |
#   <a href="/players">PLAYERS</a>
# </div>

# {% block content %}
# {% endblock %}

# </body>
# </html>


# 2. all_players.html
# the players are put in div element and the links become list items with onclick attributes
# we also want to remove navigation because its now part of master template
# {% extends "master.html" %}

# {% block title %}
#   My  Club - List of all players
# {% endblock %}


# {% block content %}
#   <div class="mycard">
#     <h1>Members</h1>
#     <ul>
#       {% for x in myplayers %}
#         <li onclick="window.location = 'details/{{ x.id }}'">{{ x.firstname }} {{ x.lastname }} {{x.age}}</li>
#       {% endfor %}
#     </ul>
#   </div>
# {% endblock %}


# 3. details.html
# we will put the player details in a div elemment and remove the link to players because thats now part of navigation in master template
# {% extends "master.html" %}

# {% block title %}
#   Details about {{ myplayer.firstname }} {{ myplayer.lastname }}
# {% endblock %}

# {% block content %}
#   <div class="mycard">
#     <h1>{{ myplayer.firstname }} {{ myplayer.lastname }}</h1>
#     <p>Phone {{ myplayer.phone }}</p>
#     <p>Player since: {{ myplayer.joined_date }}</p>
#   </div>
# {% endblock %}  


# 4. main.html

# we pit some html code into a div element
# {% extends "master.html" %}

# {% block title %}
#   My  Club
# {% endblock %}

# {% block content %}
#   <div class="main">
#     <h1>My  Club</h1>

#     <h3>Players</h3>
  
#     <p>Check out all our <a href="players/">players</a></p>
#   </div>
# {% endblock %}



# collect static files
#since there have been some changes on in mystyles.css file we need to collect the static files we have to run the collectstatic command
# python manage.py collectstatic
#run the server and check the changes