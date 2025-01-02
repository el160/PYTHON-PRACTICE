# its the process of converting a variable from one data type to another data type
# int() - converts any data type into integer type
# float() - converts any data type into float type
# ord() - converts characters into integer
# hex() - converts integer to hexadecimal string
# oct() - converts integer to octal string
# tuple() - this function is used to convert to a tuple
# set() - this function returns the type after converting to set
# list() - this function is used to convert any data type to a list type
# dict() - this function is used to convert a tuple of order (key,value) into a dictionary
# str() - this function is used to convert an integer to a string
# complex(real,imag) - this function converts real numbers to complex(real,imag
# bool() - this function is used to convert any value to a Boolean value (True or False)
# chr() - this function converts integer to character
# bin() - converts integer to binary string
# bytearray() - returns an array of bytes
# memoryview() - returns a memory view object

# Example 1
age = 5
name = 'byu'
gpa = 3.5
weight = 60.5
print(type(float(age)))


# Example 2
age = float(5)
print(age)

weight = int(60.5)
print(weight)


# Example 3
print(ord('A'))
print(ord('a'))


# Example 4
print(hex(56))
print(hex(100))

# Example 5
name = str(5)
print(name)


name = bool(name)
print(name)
