# static files in the project are handled directly when django is set to false 
# when debug is set to true, the static files are handled by the django server
# when debug is set to false, the static files are handled by the whiteNoise middleware


# Collect Static Files
# to collect all necessary static files in the project, start by specifying the static root in the settings.py file
#this specifies a folder where you want to collect your static files
# you can call the folder anything you want, we will call "productionfiles"
# STATIC_ROOT = BASE_DIR / 'productionfiles'

# STATIC_URL = 'static/'

# you can manually create the folder in the project directory or run the following command in the terminal
# "python manage.py collectstatic"

#thi willl collect all the static files in the project and store them in the specified folder
# the folder can be used to serve static files in production
# the command can bring around 131 files in the project because the admin user interface comes with builtin django that comes with css,javascript and images