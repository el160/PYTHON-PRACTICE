#using append method aad items at the end of the list
numbers = [21,34,65,76]

numbers.append(16)

print(numbers)


#using extend to add other list to a list

prime_numbers = [2,3,5]

even_numbers = [4,6,8]

prime_numbers.extend (even_numbers)

print(prime_numbers)


# slicing lists

languages = ['python','c++','dart','javascripto','hello']

print(languages[3])

myList = ['python','javascript','hello']
print(myList[1:5])

myList = ['p','y','t','h','o','n']
print(myList[1:5])

#mutable list 

car = ['mercedes','nissan','hyundai']

car[2] = 'bmw'

print(car)

#deleting items from a list
lion = [ 1,3,5,7,8,9]
lion.pop()# remove last item
print(lion)

lion.copy()#coppy entire list
print(lion)

print(lion.index(3))# print items at first occurance of index3

lion.sort()
print(lion)#prints item in order

lion.reverse()#reverses the list
print(lion)

lion.insert(1,2) #inserts 2 at index 1
print(lion)

# print(lion.count())


#list comprehension

numbers = [number*number for number in range(1,6)] # number is raised to power of 2 ie 1,2,3,4,5
print(numbers)
