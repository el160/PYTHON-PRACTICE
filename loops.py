# WHILE LOOPS
# A while loop is a control flow statement that allows code to be executed repeatedly for as long as the conditon is true
# i = 1
# while i <= 5:
#     print(i)
#     i += 1
# # using the break statement to stop the loop
# x = 1
# while x < 6:
#     print(x)
#     if x == 3:
#         break
#     x += 1
    
#     #using the continue statement to stop current iteration and go next 
#     y = 0
#     while y < 7:
#         y += 1
#         if y == 5:
#             continue
#         print(y)
        
    
# #using the else statement

# i = 1
# while i <= 5:
#     print(i)
#     i += 1
# else:
#     print('i is less than 5')
    
    
# ###FOR LOOPS
# # A for loop is a control flow statement that allows code to be executed repeatedly for each item in lists,tuples,sets etc

# fruits = ['orange','mango','jerry']
# for x in fruits:
#     print(x)
#     #using the enumerate function to get the index and value of each item in the list
#     for i, x in enumerate(fruits):
#         print(x)
# #using the break statement to stop the loop exit the loop when x is mango
# fruits = ['orange','mango','jerry']
# for x in fruits:
#     if x == 'mango':
#         break
#     print(x)
    
# #using break stament to stop the loop when x is banana and print the value of x before break
# fruits = ['orange','mango','banana','jerry']
# for x in fruits:
#     print(x)
#     if x == 'banana':
#         break
    
# #using the continue statement to skip the current iteration and go to the next one
# fruits = ['orange','mango','banana','jerry']
# for x in fruits:
#     if x == 'mango':
#         continue
#     print(x)
    
# using range in for loop here it starts from zero by default
for x in range(6):
     print(x)

# specifying the index
for y in range(2,8):
    print(y)
    
#adding a third value that specifies how a loop should be incremented
for z in range(3,30,2):
    print(z)
#using else to show that the loop has ended
for x in range(6):
    print(x)
else:
    print("The loop has ended")
    
#using the break statement to exit the loop and the else statement to show that the loop has ended
for x in range(1,6):
    print(x)
    break
else:
    print("The loop is over")
    
#nested loops ie a loop inside another loop
fruits = ['apple','banana','cherry']
colors = ['red','green','blue']
for fruit in fruits:
    for color in colors:
        print(fruit,color)
        
#using pass statement when there is no content in for loop so as to avoid getting an error
for x in range(6):
    pass