#methods,functions,operators etc of the same name that can be executed on many objects and classes
# for instance len() is a function that can be used on many objects like strings,lists,tuples etc

fruits = ["apple", "banana", "cherry"]
print(len(fruits))  # Output: 3

#we can create different classes with the same function name(importance) but with different parameters

class Fruit:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity
    def importance(self):
        return f'The fruit {self.name} is important because it has {self.quantity} quantity'
        
    
class Vegetable:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity
    def importance(self):
        return f'The vegetable {self.name} is important because it has {self.quantity} quantity'
    
class FruitBasket:
    def __init__(self, name , quantity):
        self.name = name
        self.quantity = quantity
    def importance(self):
        return f'The FruitBasket {self.name} is marvellous because it has {self.quantity} quantity'
    
fruit1 = Fruit('orange','many')
#print(fruit1.importance())  # Output: The fruit orange is important because it has many
Vegetable1 = Vegetable('potato','few')
#print(Vegetable1.importance())  # Output: The vegetable potato is important because it
FruitBasket1 = FruitBasket('basket','many')
#print(FruitBasket1.importance())  # Output: The FruitBasket basket is marvellous
for x in [fruit1, Vegetable1, FruitBasket1]:
    print(x.importance())  
    
    
# inheritance class polymorphism

class Person:
    def __init__(self, race, gender,color):
        self.race = race
        self.gender = gender
        self.color = color
    def description(self):
        return f'{self.race} is {self.gender} and is{self.color} color'

class Child(Person):
    def description(self):
        return f'The child is {self.race} and is {self.gender} and is {self.color} color'
class Adult(Person):
    def description(self):
        
        return f'The adult is {self.race} and is {self.gender} and is {self.color} color'
    
Person1 = Person('African','male','black')
Child1 = Child('Asian','female','yellow')
Adult1 = Adult('European','male','white')

for i in [Person1,Child1,Adult1]:
    print(i.description())
        
    
    