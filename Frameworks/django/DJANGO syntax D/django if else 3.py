# if statement checks if a condition is true and executes block of code
#{% if greeting == 1 %}
#   <h1>Hello</h1>
# {% endif %} 


     # Elif
# The elif keyword says "if the previous conditions were not true, then try this condition".

# Example
# {% if greeting == 1 %}
#   <h1>Hello</h1>
# {% elif greeting == 2 %}
#   <h1>Welcome</h1>
# {% endif %} 


#           Else
# The else keyword catches anything which isn't caught by the preceding conditions.

# Example
# {% if greeting == 1 %}
#   <h1>Hello</h1>
# {% elif greeting == 2 %}
#   <h1>Welcome</h1>
# {% else %}
#   <h1>Goodbye</h1>
# {% endif %} 
   
   
   
# OPERATORS USED

1.# ==
# Is equal to.

# Example
# {% if greeting == 2 %}
#   <h1>Hello</h1>
# {% endif %} 

2.# !=
# Is not equal to.

# Example
# {% if greeting != 1 %}
#   <h1>Hello</h1>
# {% endif %} 

3.# <
# Is less than.

# Example
# {% if greeting < 3 %}
#   <h1>Hello</h1>
# {% endif %} 

4.# <=
# Is less than, or equal to.

# Example
# {% if greeting <= 3 %}
#   <h1>Hello</h1>
# {% endif %} 

5.# >
# Is greater than.

# Example
# {% if greeting > 1 %}
#   <h1>Hello</h1>
# {% endif %} 

6.# >=
# Is greater than, or equal to.

# Example
# {% if greeting >= 1 %}
#   <h1>Hello</h1>
# {% endif %} 

7.# and
# To check if more than one condition is true.

# Example
# {% if greeting == 1 and day == "Friday" %}
#   <h1>Hello Weekend!</h1>
# {% endif %} 

8.# or
# To check if one of the conditions is true.

# Example
# {% if greeting == 1 or greeting == 5 %}
#   <h1>Hello</h1>
# {% endif %} 

9.# and/or
# Combine and and or.

# Example
# {% if greeting == 1 and day == "Friday" or greeting == 5 %}
# Parentheses are not allowed in if statements in Django, so when you combine and and or operators, it is important to know that parentheses are added for and but not for or.

# Meaning that the above example is read by the interpreter like this:

# {% if (greeting == 1 and day == "Friday") or greeting == 5 %}


10.# in
# To check if a certain item is present in an object.

# Example
# {% if 'Banana' in fruits %}
#   <h1>Hello</h1>
# {% else %}
#   <h1>Goodbye</h1>
# {% endif %} 


11.# not in
# To check if a certain item is not present in an object.

# Example
# {% if 'Banana' not in fruits %}
#   <h1>Hello</h1>
# {% else %}
#   <h1>Goodbye</h1>
# {% endif %} 


12.# is
# Check if two objects are the same.

# This operator is different from the == operator, because the == operator checks the values of two objects, but the is operator checks the identity of two objects.

# In the view we have two objects, x and y, with the same values:

# Example
# views.py:

# from django.http import HttpResponse
# from django.template import loader

# def testing(request):
#   template = loader.get_template('template.html')
#   context = {
#     'x': ['Apple', 'Banana', 'Cherry'], 
#     'y': ['Apple', 'Banana', 'Cherry'], 
#   }
#   return HttpResponse(template.render(context, request))  
# The two objects have the same value, but is it the same object?

# Example
# {% if x is y %}
#   <h1>YES</h1>
# {% else %}
#   <h1>NO</h1>
# {% endif %}

13.# is not
# To check if two objects are not the same.

# Example
# {% if x is not y %}
#   <h1>YES</h1>
# {% else %}
#   <h1>NO</h1>
# {% endif %} 