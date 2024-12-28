# filter method is used to filter the search and allows returning of specic rows that match the search queerry

# You can use the following sql commands to filter the search
#              1. AND
# the filter method takes the arguments ass **kwargs so you filter one or more than than fileding seperating them with a comma
# eg; return records where lastname is "ljh" and id is 3
# from django.http import HttpResponse
# from django.template import loader
# from .models import Player

# def testing(request):
#   mydata = Player.objects.filter(lastname='ljh', id=3).values()
#   template = loader.get_template('template.html')
#   context = {
#     'myplayers': mydata,
#   }
#   return HttpResponse(template.render(context, request))
      
# in template.html file

# <!DOCTYPE html>
# <html>
# <body>

# <p>The queryset object:</p>

# {{ myplayers }}

# <p>Loop through the items:</p>

# <table border='1'>
#   <tr>
#     <th>ID</th>
#     <th>Firstname</th>
#     <th>Lastname</th>
#   </tr>
#   {% for x in myplayers %}
#     <tr>
#       <td>{{ x.id }}</td>
#       <td>{{ x.firstname }}</td>
#       <td>{{ x.lastname }}</td>
#     </tr>
#   {% endfor %}
# </table>

# </body>
# </html>             


#     2.OR
# we use multiple filter () methods , seperated by a pipe | character
# the results will merge into one model
# eg return records where lastname is "ljh" or id is 3
# from django.http import HttpResponse
# from django.template import loader
# from .models import Player

# def testing(request):
#   mydata = Player.objects.filter(lastname='ljh').values() | Player.objects.filter(id= 3).values()
#   template = loader.get_template('template.html')
#   context = {
#     'myplayers': mydata,
#   }
#   return HttpResponse(template.render(context, request))
      


#   3. we can use the Q object to filter the search

# from django.http import HttpResponse
# from django.template import loader
# from .models import Player
# from django.db.models import Q

# def testing(request):
#   mydata = Player.objects.filter(Q(firstname='ljh') | Q(firstname='byu')).values()
#   template = loader.get_template('template.html')
#   context = {
#     'myplayers': mydata,
#   }
#   return HttpResponse(template.render(context, request))

# in template.html file

# <!DOCTYPE html>
# <html>
# <body>

# <p>The queryset object:</p>

# {{ myplayers }}

# <p>Loop through the items:</p>

# <table border='1'>
#   <tr>
#     <th>ID</th>
#     <th>Firstname</th>
#     <th>Lastname</th>
#   </tr>
#   {% for x in myplayers %}
#     <tr>
#       <td>{{ x.id }}</td>
#       <td>{{ x.firstname }}</td>
#       <td>{{ x.lastname }}</td>
#     </tr>
#   {% endfor %}
# </table>

# </body>
# </html>                 
        



     
     
     # Field lookups
#  these are keywords that represents specific Sql keywords
# they are used to filter the search
# eg; return records where lastname starts with "l"
# use the __startswith keyword
#'.filter(lastname__startswith='l');'

# the SQL equivalent for the statement above is
# SELECT * FROM Player WHERE lastname LIKE 'l%';

#                  Field Lookup Syntax

# all fiel lookups must be specified with fieldname followed by two(!) underscores and the lookup type
#eg return records where firstname starts with "l"
# from django.http import HttpResponse
# from django.template import loader
# from .models import Player

# def testing(request):
#   mydata = Player.objects.filter(firstname__startswith='L').values()
#   template = loader.get_template('template.html')
#   context = {
#     'myplayers': mydata,
#   }
#   return HttpResponse(template.render(context, request))


# Filed Lookups Reference
# Keyword	Description
# contains	Contains the phrase
# icontains	Same as contains, but case-insensitive
# date	Matches a date
# day	Matches a date (day of month, 1-31) (for dates)
# endswith	Ends with
# iendswith	Same as endswidth, but case-insensitive
# exact	An exact match
# iexact	Same as exact, but case-insensitive
# in	Matches one of the values
# isnull	Matches NULL values
# gt	Greater than
# gte	Greater than, or equal to
# hour	Matches an hour (for datetimes)
# lt	Less than
# lte	Less than, or equal to
# minute	Matches a minute (for datetimes)
# month	Matches a month (for dates)
# quarter	Matches a quarter of the year (1-4) (for dates)
# range	Match between
# regex	Matches a regular expression
# iregex	Same as regex, but case-insensitive
# second	Matches a second (for datetimes)
# startswith	Starts with
# istartswith	Same as startswith, but case-insensitive
# time	Matches a time (for datetimes)
# week	Matches a week number (1-53) (for dates)
# week_day	Matches a day of week (1-7) 1 is sunday
# iso_week_day	Matches a ISO 8601 day of week (1-7) 1 is monday
# year	Matches a year (for dates)
# iso_year	Matches an ISO 8601 year (for dates)



