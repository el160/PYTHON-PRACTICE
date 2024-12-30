#there are two methos of including bootstrap5 in your project:
# 1.downloading the required files and include them in your project
# 2.install the bootstrap5 module in venv of your project
# navigate to venv folder and activate the venv
# inside the venv install bootstrap5 "pip install django-bootstrap-v5"




#           update settings
# include the bootstrap module in the installed_apps list
# INSTALLED_APPS = [
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#     'players',
#     'bootstrap5',
# ]


# remove the old styling



#       Add Bootstrap 5 to Template
# in the master.html template

# <!DOCTYPE html>
# <html>
# <head>
#   <title>{% block title %}{% endblock %}</title>
#   {% load bootstrap5 %}
#   {% bootstrap_css %}
#   {% bootstrap_javascript %}
# </head>
# <body>

# <div class="container">
#   <ul class="nav bg-info">
#     <li class="nav-item">
#       <a class="nav-link link-light" href="/">HOME</a>
#     </li>
#     <li class="nav-item">
#       <a class="nav-link link-light" href="/players">PLAYERS</a>
#     </li>
#   </ul>

#   {% block content %}
#   {% endblock %}
# </div>
# </body>
# </html>