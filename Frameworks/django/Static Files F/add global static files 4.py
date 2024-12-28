#what if other applications need to use the same style sheet?
#The best way to handle this is to create a static directory in the project directory, and then create a subdirectory for each application that needs to use the style sheet.
#The static directory should be at the same level as the application directories.
# we start by creating a folder on thr project's root leveland call it any name and in this case we call it "mytaticfiles"
# my_club
#     db.sqlite3
#     manage.py
#     my_club/
#     players/
#     mystaticfiles/

# add a css file to the mystaticfiles folder in name you chose ie "myglobal.css"
#my_club
#     db.sqlite3
#     manage.py
#     my_club/
#     players/
#     mystaticfiles/
#         myglobal.css

#open the css file and add the following code
# body {
#   color: aqua;
# }


#    modify the settings.py 
# you will have to tell django to look for static files in the mystaticfiles folder
# open the settings.py file and add the following code
# add a staticfiles_dirs list
# STATIC_ROOT = BASE_DIR / 'productionfiles'

# STATIC_URL = 'static/'

# STATICFILES_DIRS = [
#     BASE_DIR / 'mystaticfiles'
# ]

# in the STATICFILES_DIRS list you can list all the directories where django should look for static files
# BASE_DIR reoresents the project's root directory
#/mystaticfiles is the directory where the css file is located and its in the root directory


# modifying the template
# now you have a global css folder that can be accessed from all your applications
# you can now modify the template to use the global css file
# {% load static %}
# <!DOCTYPE html>
# <html>
# <link rel="stylesheet" href="{% static 'myglobal.css' %}">
# <body>

# {% for x in cars %}
#   <h1>{{ x }}</h1>
# {% endfor %}

# </body>
# </html>

#             collectstatic files
# run the collectstatic command to collect the new static files
# python manage.py collectstatic
# after the command accept "yes" to allow overwriting the existing files