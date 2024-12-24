# comments allows us to have sections of code that is to be ignored
# comments are not executed by the python interpreter
# comments are used to make the code more readable
# <h1>Welcome Home</h1>
# {% comment %}
#   <h1>Fairwell ladies and gentlemen</h1>
# {% endcomment %}

#              comment description
#you can add a message to your comment to help you remember what you were doing when you wrote the code
# <h1>Welcome Home</h1>
# {% comment "this is the original welcome message" %}
#     <h1>Fairwell ladies and gentlemen</h1>
# {% endcomment %}


#          smaller comment
# you can also add a smaller comment to your code by using the {# #} syntax
# <h1>Welcome Home{# Everyone#}</h1>

#      Comments in views
from django.http import HttpResponse
from django.template import loader

def testing(request):
  template = loader.get_template('template.html')
  #context = {
  # 'var1': 'jack',
  #}
  return HttpResponse(template.render())
