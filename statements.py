a = 3,
b = 7,
if a > b:
 print("a is less than b")

elif a != b:
 print("a is not equal to b")

else  :
 print("a is less than b")

#shorthand
if a > b : print("a is not greater than b")

print("a") if a > b else print("b")  #if a > b then print a else print b


# logical 
if a < b and b > a: print("logical is true")

if a > b or a != b: print("logical might true")  #if a > b or a == b then print true

if not a == b : print("logical not true")

## nested if 

y = 300

if y > 100:
    print("y is greater than 100")
if y < 200:
        print("false")
else : print("y is greater")


#python calculator

Operator = input("Enter the operator(+ - * /): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if Operator == "+":
    result = num1 + num2
    print(round(result, 2))
elif Operator == "-":
    result = num1 - num2
    print(round(result, 2))
elif Operator == "*":
    result = num1 * num2
    print(round(result, 2))
elif Operator == "/":
    result = num1 / num2
    print(round(result, 2))
else:
    print("Invalid Operator")
    
    
    #python weight converter
weight = float(input("Enter your weight: "))
unit = input("Enter the unit kilograms or pounds? (K or L): ")



if unit == "K":
    converted = weight / 0.45
    unit = "lbs"
    print(f"Your weight is {round(converted,1)} lbs")
elif unit == "L":
    converted = weight * 0.45
    unit = "kg"
    print(f"Your weight is {round(converted,1)} kg")
else:
    print(f"the {unit} is not valid")
    
    
    # temeperature converter
unit = input("Enter the unit celsius or fahrenheit? (C or F): ")
temp = float(input("Enter the temperature: "))
if unit == "C":
    converted = round((temp * 9/5) + 32,1)
    unit = "F"
    print(f"Your temperature is {round(converted,2)} F")
elif unit == "F":
    converted = round((temp - 32) * 5/9,1)
    unit = "C"
    print(f"Your temperature is {round(converted,2)} C")
else:
    print(f"the {unit} is not valid")

