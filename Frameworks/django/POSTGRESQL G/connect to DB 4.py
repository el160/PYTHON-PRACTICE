# to make django connect to DB you have to specify it in the settings.py file
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'my-djnago1',
#         'USER': 'byu23',
#         'PASSWORD': '12345678',
#         'HOST': 'w3-django-project.cdxmgq9zqqlr.us-east-1.rds.amazonaws.com',
#         'PORT': '5432'
#     }
# 


#           Engine
#in settings.py file we insert postgresql instead of sqlite

#            NAme
# if no name given to the database the provider accepts "postgress" as the name of the databse


#         Username And Password

# insert the username and pasword you specified when you created the DB

#              Host? Port?
# Host and port can be found under the connectivity & security section in the RDS instance


#                     Migrate

#once done with the changes in settings.py ,run migration in venv,before changes take place
#"py manage.py migrate"

# once done run the server 