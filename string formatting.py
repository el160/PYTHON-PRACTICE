# f formatting of strings
price = 70
text = f"Price is ${price}"
print(text)

#using a modifier : to format the string .2f means 2 decimal places with fixed point number
price = 60
txt = f"price is ${price:.2f}"
print(txt)

#performing operations inside the place holder
price = 70
txt = f"price is ${price * 1.1:.2f}"
print(txt)

#performing math operations on variables
kiss = 40
hug = 30
union = f"union is ${kiss * hug:.2f} "# 2 stands for 2decimal places and f stands for fixed point number
print(union)

#perform if else inside place holders
price = 70
pay = f"its very  {'costly'if price >70  else   'cheap'}"
print(pay)



# string methods

#upper() method
text = "hello world"
print(text.upper()) #HELLO WORLD

#find() method
text = "hello world"
print(text.find("world")) #6
print(text.find("python")) #-1
print(text.find("o")) #4
print(text.find("o", 5)) #7
print(text.find("o", 5, 7)) #-1
print(text.rfind("o")) #7



print(help(str))# gives all the methods that can be used with strings



#               an example working with strings
#username must not be more than 10 characters
#username cant contain spaces
#username must be in lower case
#username cannot have digits
#username must contain special characters

username = input("Enter username: ")
if len(username) > 10:
    print("Username must not be more than 10 characters")
elif not username.find(" ") == -1:
    print("Username cannot contain spaces")
elif not username.islower():
    print("Username must be in lower case")
elif username.isdigit():
    print("Username cannot have digits")
elif not username.find("@") == -1:
    print("Username must contain special characters")
else:
    print(f"Hello {username} welcome to the system")
