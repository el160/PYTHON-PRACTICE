# vitrual env is an environment used by django to excute an application
# its reccommended to create and execute django application in a seperate virtula environment

#    setting up virtual environment
#1. install python3-venv package by using the following command.
'apt-get install python3-venv'
#2.Create a Directory
' mkdir myworld'  
#After it, change directory to the newly created directory by using the cd myworld.  

#3. create a virtual env
' py -m venv myapp  '

#4. activate the virtual environment
'myapp\Scripts\activate'

#5.install django in the virtual environment
'pip install django'