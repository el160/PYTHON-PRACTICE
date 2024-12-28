# queryset is a collection of data from the database
# QuerySet API is a powerful tool for working with models
# queryset make it easier to get data you actually need by allowing filtration and order by at an early age


# in the views.py file we can use all() method to get all the data from the database
# from django.http import HttpResponse
# from django.template import loader
# from .models import Player

# def testing(request):
#   mydata = Player.objects.all()
#   template = loader.get_template('template.html')
#   context = {
#     'myplayers': mydata,
#   }
#   return HttpResponse(template.render(context, request))

# the object is placed in a variable called mydata and its sent to the template via context object as myplayers

# now in the template.html file we can use the data
# <table border='1'>
#   <tr>
#     <th>ID</th>
#     <th>Firstname</th>
#     <th>Lastname</th>
#   </tr>
#   {% for x in myplayers %}
#     <tr>
#       <td>{{ x.id }}</td>
#         <td>{{ x.firstname }}</td>
#       <td>{{ x.lastname }}</td>
#     </tr>
#   {% endfor %}
# </table>