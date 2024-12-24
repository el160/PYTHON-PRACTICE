# for loop is used to iterate over a sequence (list, tuple, dictionary, set, string)


#         Daata in a model
# when we get data from a model it becomes a queeryset and we can loop through it:
# a model is basically data in a database in form of tables,rows &columns
# <QuerySet[{
#     'id': 1,
#     'firstname': 'John',
#     'lastname': 'Doe',
#     'age': 23,
#     'phone':1234565432 
#     'date_joined:' '2021-06-06'
# }
# {  'id': 2,
#     'firstname': 'Jane',
#     'lastname': 'Doe',
#     'age': 23,
#     'phone':1234565432
#     'date_joined:' '2021-06-06'
    
# }]>

#        we can loop through fetched data using a for loop
# {% for x in players %}
# <h1>{{ x.id }}</h1>
# <p>
# {{ x.firstname }} 
# {{ x.lastname }} 
# {{ x.age }} 
# </p>
# {% endfor %}

#           Reversed keyword  for loop
# the reversed keyword is used when we want to do loop in reversed order
# {% for x in players reversed %}
# <h1>{{ x.id }}</h1>
# <p>
# {{ x.firstname }}
# {{ x.lastname }}
#</p>
# {% endfor %}

#           Empty keyword for loop
# used if you want to do something special if the object is empty
# {% for x in emptyobject %}
# <li>{{ x.firstname }}</li>
#   {% empty %}
#     <li>No members</li>
#   {% endfor %}
# </ul> 

          # empty keyword can also be used if the object does not exist
#   <ul>
#   {% for x in myobject %}
#     <li>{{ x.firstname }}</li>
#   {% empty %}
#     <li>No members</li>
#   {% endfor %}
# </ul>      



            # Loop Variables
# the loop variables are used to get the current iteration of the loop
   #1. forloop.counter: returns the number of times the loop has run
   ## current iteration starts from 1
#    

#2.forloop.counter0
# current iteration starts from 0
# <ul>
#   {% for x in fruits %}
#     <li>{{ forloop.counter0 }}</li>
#   {% endfor %}
# </ul> 
# # 

#3 forloop.first
#allows you to test if the current iteration is the first iteration
# <ul
#   {% for x in fruits %}
#     <li
#       {% if forloop.first %}
#         style='background-color:lightblue;'
#       {% endif %}
#     >{{ x }}</li>
#   {% endfor %}
# </ul> 

#4 forloop.last
# allows you to test if the current iteration is the last iteration
# <ul>
#   {% for x in fruits %}
#     <li
#       {% if forloop.last %}
#         style='background-color:lightblue;'
#       {% endif %}
#     >{{ x }}</li>
#   {% endfor %}
# </ul> 

#5 forloop.revcounter
# returns the number of times the loop has run in reverse order
# the current iteration if you start at the end and count backwards ending at 1
# <ul>
#   {% for x in fruits %}
#     <li>{{ forloop.revcounter }}</li>
#   {% endfor %}
# </ul> 

#6 forloop.revcounter0
# returns the number of times the loop has run in reverse order
# <ul>
#   {% for x in fruits %}
#     <li>{{ forloop.revcounter0 }}</li>
#   {% endfor %}
# </ul> 