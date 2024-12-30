#inside the RDS create a database or just navigate to database section and click the "create database button"
#                   SETTINGS
# once you started creating a databse you will be given some choices for type and settings of ur database
# choose the following options
# 1. standard connection method:
         #standard create

#2. postgreSQL engine method:
          #PostgreSQL 
          
#3. Free Tier template
       # free tier
       
#4. Name of database,username, password (choose any)
     # name of DB instance: my-django1
     # master username: byu23
     #master  password: 12345678
     
#5. keep the default instance configuration
       # burstable classes(includes t classes)
       
#6. check off the storage autoscalling
     # its not bad to enable the autoscalling
     
#7. Grant public access and create a new security group
      # give a security group name we will call it project-1
      # select dont connect to an EC2 computer resource
      #VPC(virtual private cloud) -defaul
      #DB subnet group - default
      #publicly accessible - yes
      #VPC security group(firewall)-create new
      #security group name - project-1
      # availability Zone -no preference
      
#8. keep default db authentications
       # databae auth options- password auth
       
#9. keep default monitoriing
   # turn on performance insights
   #retention period - 7days(free tier)
   #AWS KMS -default
   
#10. click create database button
      