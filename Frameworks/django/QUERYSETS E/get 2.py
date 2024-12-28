# there are specific methods that can be used to get a single record from the database

#               1.values() method
# this methods allow you to return objects as python dictionaries with the name & values as keys/pairs

# from django.http import HttpResponse
# from django.template import loader
# from .models import Player

# def testing(request):
#   mydata = Player.objects.all().values()
#   template = loader.get_template('template.html')
#   context = {
#     'myplayers': mydata,
#   }
#   return HttpResponse(template.render(context, request))

#            2.values_list() method
# allows you to return only the columns that you specify
# from django.http import HttpResponse
# from django.template import loader
# from .models import Player

# def testing(request):
#   mydata =  Player.objects.values_list('first_name', 'last_name')
#   template = loader.get_template('template.html')
#   context = {
#     'myplayers': mydata,
#   }
#   return HttpResponse(template.render(context, request))

#            3.filter() method
#allows you to return specific rows/records that you want
# from django.http import HttpResponse
# from django.template import loader
# from .models import Player

# def testing(request):
#   mydata = Player.objects.filter(firstname='byu').values()
#   template = loader.get_template('template.html')
#   context = {
#     'myplayers': mydata,
#   }
#   return HttpResponse(template.render(context, request))