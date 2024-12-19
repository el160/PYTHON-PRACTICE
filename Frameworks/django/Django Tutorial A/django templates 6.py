# contains html files that displays more of app info
# usually created in the app folder (players)
#navigate the app folder and create a folder named templates then inside the templates create a file named first.html
# structure should look like :
# my_club
#     manage.py
#     my_club/
#     players/
#         templates/
#             first.html

# open the html file and insert code to display the app info
# % static loader%
# <!DOCTYPE html>
# <html>
# <body>

# <h1>Hello World!</h1>
# <p>Welcome to my first Django project!</p>

# </body>
# </html>


#open the views.py folder in the project my_club and replace players(app) with:
# from django.http import HttpResponse
# from django.template import loader

# def players(request):
#   template = loader.get_template('first.html')
#   return HttpResponse(template.render())


# go to settings.py file of the project folders
#go to installed apps sections  and add the app (players)
# INSTALLED_APPS = [
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#     'players'
# ]

# then run the command "python manage.py migrate" which will show all migrations
# Operations to perform:
#   Apply all migrations: admin, auth, contenttypes, sessions
# Running migrations:
#   Applying contenttypes.0001_initial... OK
#   Applying auth.0001_initial... OK
#   Applying admin.0001_initial... OK
#   Applying admin.0002_logentry_remove_auto_add... OK
#   Applying admin.0003_logentry_add_action_flag_choices... OK
#   Applying contenttypes.0002_remove_content_type_name... OK
#   Applying auth.0002_alter_permission_name_max_length... OK
#   Applying auth.0003_alter_user_email_max_length... OK
#   Applying auth.0004_alter_user_username_opts... OK
#   Applying auth.0005_alter_user_last_login_null... OK
#   Applying auth.0006_require_contenttypes_0002... OK
#   Applying auth.0007_alter_validators_add_error_messages... OK
#   Applying auth.0008_alter_user_username_max_length... OK
#   Applying auth.0009_alter_user_last_name_max_length... OK
#   Applying auth.0010_alter_group_name_max_length... OK
#   Applying auth.0011_update_proxy_permissions... OK
#   Applying auth.0012_alter_user_first_name_max_length... OK
#   Applying sessions.0001_initial... OK

# (myworld) C:\Users\Your Name\myapp\my_club>

#N/B virtula env has to be active (myapp)

#navigate to the project folder and run the serever 


