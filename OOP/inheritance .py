# creates a parent class whereby the child class inherits properties
#we do this to avoid code repetition

class Vehicle:
    def __init__(self,color,brand,year):
        self.color =color
        self.brand = brand
        self.year = year
        
#creating a method
def description(self):
    print(self.color,self.brand,self.year)
    
#creating an object
car = Vehicle('red','Toyota',2015)
#calling the method
car.description()

#creating a child class

