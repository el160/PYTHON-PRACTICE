# i django templates we render variables by putting them inside {{}} brackets
#<h1>Hello {{ firstname }}, how are you?</h1>



#           Ceating a variable in a view
# we can creste variable firstname that can be sent to template via view in views.py file
# we create an object named context ,fill the variable details and send it as first parameter in the template.render() function
# from django.http import HttpResponse
# from django.template import loader

# def testing(request):
#   template = loader.get_template('template.html')
#   context = {
#     'firstname': 'elijah',
#   }
#   return HttpResponse(template.render(context, request))

#                  Create variable in Template
# we use {% with%} template tag 
# we end tag by {%endwith%} tag

# {% with firstname= "elijah"%}
# <p> Heloo {{firstname}}, how are you?</P>
# {%endwith%}




#            Data from a model
#the Player model created in the previous chapters , to get data from it we have to import it in the views.py
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Player

def testing(request):
  myplayers = Player.objects.all().values()
  template = loader.get_template('template.html')
  context = {
    'myplayers':myplayers,
  }
  return HttpResponse(template.render(context, request))

# now the data above can be used in a template

# <ul>
#   {% for x in myplayers %}
#     <li>{{ x.firstname }}</li>
#   {% endfor %}
# </ul>

# we use tdjango tag {%for%} to loop through the players