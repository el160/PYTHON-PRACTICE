# when creating web applications we need to add static files to our project likw images and css files
#start creating a folder in your project directory called static in the same directory as your manage.py filewhere you created the templates folder
# my_club
#     manage.py
#     my_club/
#     players/
#         templates/
#         static/

#add a css file to the static folder called first.css
#my_club
#     manage.py
#     my_club/
#     players/
#         templates/
#         static/
#             first.css

#add the following code to the first.css file
# body {
#   background-color: magenta;
#   font-family: verdana;
# }


#include the css file in the html file
#open the html file and add the following code {% load static %}
# in the head section of the html file add the following code
#<link rel="stylesheet" href="{% static 'first.css' %}">

# {% load static %}
# <!DOCTYPE html>
# <html>
# <link rel="stylesheet" href="{% static 'myfirst.css' %}">
# <body>

# {% for x in cars %}
#   <h1>{{ x }}</h1>
# {% endfor %}

# </body>
# </html>

# restert the server for the changes to take effect
