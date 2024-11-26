numbers = [1, 2, 3, 4, 5]

# Accessing items
print(numbers[0])  # returns the first item: 1
print(numbers[1])  # returns the second item: 2
print(numbers[-1]) # returns the first item from the end: 5
print(numbers[-2]) # returns the second item from the end: 4

#Modifying the list
numbers.append(6)     # Adds 6 to the end: [1, 2, 3, 4, 5, 6]
numbers.insert(0, 6)  # Inserts 6 at index 0: [6, 1, 2, 3, 4, 5, 6]
numbers.remove(6)     # Removes the first occurrence of 6: [1, 2, 3, 4, 5, 6]
numbers.pop()         # Removes the last item: [1, 2, 3, 4, 5]
numbers.clear()       # Clears the entire list: []

# Other list methods
numbers = [3, 1, 4, 5, 2]
numbers.sort()        # Sorts the list: [1, 2, 3, 4, 5]
numbers.reverse()     # Reverses the list: [5, 4, 3, 2, 1]
numbers.copy()        # Returns a copy of the list

# Checking the index of an item
print(numbers.index(3)) # Returns the index of the first occurrence of 3
