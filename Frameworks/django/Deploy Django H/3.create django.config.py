# on the rooot level of the project create a folder called ".ebextensions"
#my_club
    # .ebextensions/
    # players/
    # my_club/
    # mystaticfiles/
    # productionfiles/
    # db.sqlite3
    # manage.py
    # requirements.txt
    
# in the .ebextensions folder create a file called "django.config"
# my_club
    # .ebextensions/
    #     django.config
    
#open the django.config file and insert the following settings
# option_settings:
#   aws:elasticbeanstalk:container:python:
#     WSGIPath: my_club.wsgi:application


#wrap the dependancies into one .zip file