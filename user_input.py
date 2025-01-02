# a function that prompts the user to enter data and returns the entered data as a string


#input("Hello how are you?:")
name = input("Enter your name:")
age = input("Enter your age:")
age = int(age)
age = age + 1

print(f'Hello {name} ')
print('Happy Birthday')
print(f'You are now {age} years old')

# simple calculator
lenght = input("Enter the lenght of the rectangle:")
width = input("Enter the width of the rectangle:")
area = float(lenght) * int(width)
print(f'The area of the rectangle is {area}m^2')


# simple shopping cart
item = str(input("Enter the item you will like to buy:"))
quantity = int(input("how many will you like:"))
price = float(input("the price of each item is :"))
total = quantity * price

print(f"You have bought{quantity}{item}/s at the rate of ${price} each")
print(f"The total cost is {total}")
print("Thank you for shopping with us")


# madlibs game
noun1 = input("Enter a noun(person, place or thing):")
verb = input("Enter a verb (action word): ")
adjective1 = input("Enter an adjective(description):")
noun2 = input("Enter a noun(person, place or thing):")
adjective2 = input("Enter an adjective(description):")

print(f"The christmas celebration was {adjective1}")
print(f"I was {verb}")
print(f"I saw {noun1}")
print(f"I danced with {noun2}")
print(f"After the party, I felt {adjective2}")
print("It was a great celebration")