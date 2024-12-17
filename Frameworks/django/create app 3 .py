# an a pp is a web application that has a specific meaning in your project eg home page,database etc
# name the app for instance "players"
# navigate the project project folder ie cd my_club
# create a new app using the following command:
# "py manage.py startapp players"

# now you have a new app in your project folder:
# my_club
#     manage.py
#     my_club/
#     players/
#         migrations/
#             __init__.py
#         __init__.py
#         admin.py
#         apps.py
#         models.py
#         tests.py
#         views.py


from django.shortcuts import render

# Create your views here.
#Find it and open it, and replace the content with this:

#my_tennis_club/members/views.py:

from django.shortcuts import render
from django.http import HttpResponse

def members(request):
    return HttpResponse("Hey players!")