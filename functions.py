# defining a function 
def my_function ():
    print("Hello welcome on board")

my_function()  # calling the function
    
def my_function (fname):
    print(fname + " is my name")
my_function("elijah")
my_function("Nyamweya")
    
#arbitrary arguments ir when we dont know how many arguments will be
#passed we use * before the parameters
def mychild (*kid):
    print("my child is " + kid[2])
mychild("osebe", "oganchugu", "ombeki")
    
    
#keyword Arguments
def my_family(child1,child2,child4):
    print("My family is comprised of " + child1 + " " + child2 + " " + child4)
my_family(child1="Osebe",child2="Omondi",child4="Ombeki")
    

#when we know how many keywords will be passed we use ** before

def myCar (**model):
    print("my car's model is " + model["make"])
myCar(make="Germany", model="Japan", age="USA")

#default parameter value
def myKin (myorigin = "Nyanza"):
    print ("i come from" + " " + myorigin)
myKin("Eastern")
myKin("Rift valley")
myKin("Central")
myKin()

#passing a list as an argument
def my_family (child):
    for i in child:
        print(i)
names=['john','jack','luke','meow']
my_family(names)

# leting a function return a value we use the return statement
def myfunction (y):
    return y**2
print(myfunction(5))
print(myfunction(10))
print(myfunction(20))
print(myfunction(30))

# using pass statement when we want the function to do nothing so as to avoid errors
def myfunction():
    pass

# #positional arguments we use ,/ to define them and if no ,/ it will be automatically a keyword arguments

def myNumber ( y,/):
    print(y)
myNumber(2)

# if we use ,/ then pass it as a keyword argument we will get an error
# def myNumber ( y,/):
#     print(y)
# myNumber( y = 2)

#keyword position only arguments we use *, before the values
def myNumber (*,y):
    print(y )
myNumber(y = 4)


## combining positional and keyword arguments

def myAdds (x,y,/,*,h,n):
    print(4+6+9+7)
myAdds(4,6,h=9,n=7)

# function recursion
#means that a defined function is calling itself
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("Recursion Example Results:")
tri_recursion(5)

