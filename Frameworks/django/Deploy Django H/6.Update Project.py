# any changes you do in the local machine are not visible in the deployed section
#inorder for the changes to be visible in the deployed section you need to redeploy the application by creating a zip file  and apploading
#select only the relevant folders
# my_club
#     .ebextensions/**
#     players/**
#     my_club/**
#     mystaticfiles/
#     productionfiles/**
#     db.sqlite3
#     manage.py**
#     requirements.txt**

# right click to make a zip file and upload to Elastic Beanstalk
# log in to AWS account and find your project under the "Elastic beanstalk " application
#click the "upload and deploy" button
#choose the zip file and upload it in "choose file" button
#click on 'deploy' button
# your updated project will uploaded