# creates a parent class whereby the child class inherits properties
#we do this to avoid code repetition

class Vehicle:
    def __init__(self,color,brand,year):
        self.color =color
        self.brand = brand
        self.year = year
        
#creating a method
    def description(self):
     print(f'color:{self.color},brand:{self.brand},year:{self.year}')
    
#creating an object
car = Vehicle('red','BMW',2015)
#calling the method
car.description()

#creating a child class
class Bike(Vehicle):
    def __init__(self, color, brand, year):
        super().__init__(color, brand, year)# super method makes sure that the parent class properties are called and not overrided by child class properties
        self.wheels = 2 #adding a new property to the child class thats not in parent class
        
#adding new method to bike
    def feature(self):
     print(f'this bike has {self.wheels} wheels')
    
#creating and oblect of child class
cycle = Bike('white','Honda',2019)
#calling the method
cycle.description()
cycle.feature()
        
