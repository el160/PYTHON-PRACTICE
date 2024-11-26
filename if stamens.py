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