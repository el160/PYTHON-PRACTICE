# constructor __init__ allow each object to have and start with specific values
#instance variables change the state of an object and they do vary

class Dog:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

# create two  objects with unique attributes
my_dog1 = Dog("Buddy", 3, "Golden Retriever")
my_dog2 = Dog("Max", 2, "Poodle")
print(f'my dog is called {my_dog1.name} and its {my_dog1.age} years old {my_dog1.breed}')
print(f'my dog is called {my_dog2.name} and its {my_dog2.age} years old {my_dog2.breed}')
if my_dog1.age > my_dog2.age:
    print(f'{my_dog1.name} is older than {my_dog2.name}')
else:
    print(f'{my_dog2.name} is older than {my_dog1.name}')
print("all dogs are good")