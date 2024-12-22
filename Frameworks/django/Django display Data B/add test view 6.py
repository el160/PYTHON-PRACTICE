# when testing different aspects of django , it's good to have a separate place for testing without destroying the mainobject


# start by adding a testing code in the views.py
# def testing(request):
#   template = loader.get_template('template.html')
#   context = {
#     'colors': ['black', 'Magenta', 'Yellow'],   
#   }
#   return HttpResponse(template.render(context, request))


# go the urls.py of the app folder and add the testing path
#this is to ensure that incoming urls to /testing will be redirected to testing view
# path('testing/', views.testing, name='testing'), 

#         Test template
# we need atest html file where we can play with html and django
# create a new file called template.html in the templates folder of the app folder ad add the following code
# <!DOCTYPE html>
# <html>
# <body>

# {% for x in fruits %}
#   <h1>{{ x }}</h1>
# {% endfor %}

# <p>In viewpy you can notice the colors listed.</p>

# </body>
# </html>

#run the server