# multi doulble strings we use """ or '''

message = """
hello biyu
como estas
moi bien
"""
print(message)

#compare two strings using == operator

String1 = 'Hello Plp'
String2 = 'Heloo can i have your number'
String3 = 'Whats your name precisely'

print(String1==String2) #answer will be false

# join two or more strings concatenate using + operator
String2 = 'Heloo can i have your number'
String3 = 'Whats your name precisely'
result = String2 + String3
print(result)

#iteration through strings

dog = 'Barks'
for letter in dog:
    print(letter)

# escape sequences in python we use the backslash \

message = "he said,\"whats is your name\""
print(message)

memory = 'he said, \"whats is your name\"'

#formating strings (f-strings)
name = "Byu"
origin = "Nanyuki"
print(f'{name} is from {origin}')
