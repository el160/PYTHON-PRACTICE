# there are several ways of connectiing to db but major ways are by use of SQL shell(psql) and pgAdmin 4 of which both comes with installation of POSTGRESQL



# 1.SQL shell(psql) is a terminal based interface where you can write & execute SQL synthax to interact with the database 

#a.search for sql shell on the windows search bar
#open the program and insert name of the server of which suggested name is localhost
#click enter and suggested database will be postgres
#click enter and suggested port will be 5432
# click enter and suggested username will be postgres or you can enter any name of your choice
# enter the password you entered during installation of postgresql
# the result might look like an erroe but if it shows psql(17) or any other version and at the end you see postgress=# command then the database has been successfully connected


# b. excute Sql statements
# since the databse is empty you cant querry any tables but you can check the the version using the command SELECT version()
# to insert sql statements just write them after postgress=#
#always put a semicolon after the command



#            2. pgAdmin4
#serch for pgAdmin4 in the window search bar and start the application
#once the program has started click on the servers tab and you will be prompted to enter a passowrd that you originally used durig installation
#click on the database option in the main menu
#you will find a dabase name postgress ,right click and choose the querry tool
#in the queery tool you can start executing sql statements
#write the queery sql statement command SELECT version()
# to insert Sql statements in queery tool just write in the input box
# to execute statements click on the play button above the input box
