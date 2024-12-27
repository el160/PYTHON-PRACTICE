# inorder to log in to the admin application we need to create a user with admin role
# we can do this by creating a new user and then assigning the admin role to that user
# we create a new user by the following command:
#"py manage.py createsuperuser"

# the above command will prompt us to enter the username, email and password for the new user
#Bypass password validation and create user anyway? [y/N]: y
# press enter and a superuser will be created successfully
# start the server again and redirect to /admin route 