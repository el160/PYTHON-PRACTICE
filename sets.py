#creating an empty set

car = set()
print(type(car))

#adding items to a set using add

numbers = {1, 2, 3, 4, 5}
print(numbers)

numbers.add(6)
print(numbers)

#update python set using update

mafudi = {'tall','dark',5.8,}
omondi = {'small',5.9}
mafudi.update(omondi)
print(mafudi)

#remove items from a set we use discard

languages = {'english','spanish','maasai'}

remove = languages.discard('english')

print(languages)


#sum in sets

continent ={'africa','Asia','Europe','UK','Japan'}


print(len(continent))

continent ={1,2,3,4,5,6,8}
print(sum(continent))

#iteration in sets

groceries = {'apple','mango','avocado','orange'}

for fruit in groceries:
    print(fruit)

#union sets

A = {1,3,4,67,5,34}
D = {34,76,78,45.4}

print(A|D)

print(A .union(D))

#intersection sets ie only common items will be printed

A = {1,3,4,67,5,34}
D = {34,76,78,45.4}

print(A&D)
print(A.intersection(D))

#diference sets prints sets A elements thats are not in set D we use -
A = {1,3,4,67,5,34}
D = {34,76,78,45.4}
print(A-D)
print(A.difference(D))

#symetric difference ie all elements in A and D without common elements we us ^
A = {1,3,4,67,5,34}
D = {34,76,78,45.4}
print(A^D)

# see if all sets are equal we use ==
A = {1,3,4,67,5,34}
D = {34,76,78,45.4}
if A == D:
    print('a is is equal to D')
else:
    print('A is not equal to D')
