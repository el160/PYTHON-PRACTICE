#we use apache2.conf file to configure the server  located at /etc/apache directory.
# this server can be used instead of the default django server which runs on port 8000
#Add the following code into this file(apache2.conf):
#WSGIScriptAlias / /var/www/html/django7/django7/wsgi.py  
#WSGIPythonPath /var/www/html/django7/  
  
# <Directory /var/www/html/django7>  
#    '<Files wsgi.py>  
#                 Require all granted  
#    </Files> 
# </Directory>  

# after this you can run the server by using the following command
# server apache restart
# then type localhost on the browser's address bar
# this time the project will run on apache server other than built in django server