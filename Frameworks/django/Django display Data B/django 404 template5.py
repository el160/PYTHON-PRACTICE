# django has got a default 404 error page 
# this page can be customised
# django will look for a customised 404.html in the templates directory of the app to dispaly it when ther is a 404 error
# if the 404.html is not found in the templates directory of the app, it will show "not found"
#to customise this message create 404.html and fill whatevr you want

# <!DOCTYPE html>
# <html>
# <title>Wrong address</title>
# <body>

# <h1>Ooops!</h1>

# <h2>I cannot find the file you requested!</h2>

# </body>
# </html>

# When DEBUG = False, Django requires you to specify the hosts you will allow this Django project to run from.
# This is a security feature to prevent a Django project from being run from any host.
#In production, this should be replaced with a proper domain name:

#ALLOWED_HOSTS = ['yourdomain.com']