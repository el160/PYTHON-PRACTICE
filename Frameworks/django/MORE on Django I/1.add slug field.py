# A SLUG is a description containing only letters,hyphens,numbers or underscores
# A slug is typically used as part of a URL
#typically used to make urls easier to read and make them more search engine friendly
# In creating a slug"


#      1. modify the models.py file
#open the models.py file and add a field called slug with the datatype slugfield
# from django.db import models

# class Player(models.Model):
#   firstname = models.CharField(max_length=255)
#   lastname = models.CharField(max_length=255)
#   age = models.IntegerField()
#   phone = models.IntegerField(null=True)
#   joined_date = models.DateField(null=True)
#   slug = models.SlugField(default="", null=False)

#   def __str__(self):
#     return f"{self.firstname} {self.lastname} {self.age}"

# since there has been a change in the models structure we have to make migration to tell django that it has to add to the database
#"py manage.py makemigrations"
# then the migrate command "py manage.py migrate"


#     2. Change Admin
# ther is a new field in the database but we want this field to updated automatically when we set firstname or lastname of a player
#this can be done by built in django feature called "prepopulated_fields"
#in this field you specifythe field you want to pre-populate and tuple with the fields you want to populate it with
# from django.contrib import admin
# from .models import Player

# # Register your models here.

# class PlayerAdmin(admin.ModelAdmin):
#   list_display = ("firstname", "lastname", "joined_date",)
#   prepopulated_fields = {"slug": ("firstname", "lastname")}
  
# admin.site.register(Player, PlayerAdmin)

# enter the admin interface and open record for editing
# click save and the slug field will be autopopulated with first name and lastname
#since slug field is of type SlugField it will 'slugify' the value ie it will put a hyphen between each word




#       3. Modify Template
# we will replace the ID field with the slug throughout the project
# in all_players.html where we have a link to details page
# {% extends "master.html" %}

# {% block title %}
#   My  Club - List of all players
# {% endblock %}


# {% block content %}
#   <div class="mycard">
#     <h1>players</h1>
#     <ul>
#       {% for x in myplayers %}
#         <li onclick="window.location = 'details/{{ x.slug }}'">{{ x.firstname }} {{ x.lastname }}</li>
#       {% endfor %}
#     </ul>
#   </div>
# {% endblock %}



#      4. Modify URL
#chnage from <int:id> to <slug:slug>:
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.main, name='main'),
#     path('players/', views.players, name='players'),
#     path('players/details/<slug:slug>', views.details, name='details'),
#     path('testing/', views.testing, name='testing'),
# ]


#          5. Modify View
# chnage details view to handle incoming request as a slug instead of ID
#def details(request, slug):
#   myplayer = Player.objects.get(slug=slug)
#   template = loader.get_template('details.html')
#   context = {
#     '  myplayer':   myplayer,
#   }
#   return HttpResponse(template.render(context, request))



# run the server