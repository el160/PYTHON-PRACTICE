# create a urls.py folder in the app folder (players)
#urls .py is basically used for routing 
# if you check on the projects"folder you will also see a url.py folder that
#basically connects with the urls.py folder in the app folder 
#in the url.py folder in app folder write the following command:
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('players/', views.players, name='players'),
# ]

# # go to the urls.py file in the project folder and ensure it has the following code:
# from django.contrib import admin
# from django.urls import include, path
# urlpatterns = [
#     path('', include('players.urls')),
#     path('admin/', admin.site.urls),
# ]

# if the server is not running navigate to the project folder (my_clud) and run the following command
#"py manage.py runserver"
# the message in the views.py file in the app(players) folder will be dispalyed "hey players!"