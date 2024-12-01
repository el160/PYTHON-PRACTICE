# creating a module
#create a new file called "Mymodule.py" and add the following code
def MyCar(name):
    print ("G63" + " is a great car")
    
#use the module in another file
#we use the import statement to import the module
import Mymodule
Mymodule.MyCar("G63")


#Variables in modules
#variables of all types eg dictionaries,lists,tuples etc
lady = {
    "name": "Lady Gaga",
    "age": 35,
    "city": "New York",
    "cars": ["Mercedes", "BMW", "Audi"],
}
import Mymodule
#accesing lady dictionary
a = Mymodule.lady["name"]
print(a)

#Renaming a module using "as" keyword
import Mymodule as mm
a = mm.lady["name"]
print(a)

#builtin modules
#python has a number of built-in modules that can be used to perform various tasks
import math
print(math.pi)
import platform
x = platform.system()
print(x)

#python import from function
# we can use from keyword to import part of the module  not the whole module
from math import pi
print(pi)
# importing multiple values from a module
from math import pi,sin,cos
print(pi,sin(90),cos(90))

# importing everything from a module using *
from math import *
print(pi,sin(90),cos(90))

#locating path of modules
#python searches for modules in the following locations
#1. The current working directory
#2. The list of directories passed using the -I or --install-dir option when running python
#3. The installation-dependent default paths
#4. The list of directories in the PYTHONPATH environment variable
#5. The installation-dependent default paths
#6. The list of directories in the sys.path variable
import sys
print(sys.path)