#the include tag allows you to include the contents of another template in the current template.
# this is useful when you have a block ofcontent tha is the same for many pages
#footer.html: 
# <p>Copyright 2015. All rights reserved.</p>

# main.html:
# <!DOCTYPE html>
# <html>
# <head>
#     <title>{% block title %}My amazing site{% endblock %}</title>
# </head>
# <body>
# <h1>Hello</h1>

# <p>This page contains a footer in a template.</p>

# {% include 'footer.html' %}



# Variables in templates
# you can send varaibles into templates using the with keyword and include {{}}
# <!DOCTYPE html>
# <html>
# <body>

# {% include "main.html" with me="TOBIAS" sponsor="W3SCHOOLS" %}

# <h1>Welcome</h1>

# <p>This is my webpage</p>

# </body>
# </html> 