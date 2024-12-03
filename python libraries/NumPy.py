#creating a numpy arrary
import NumPy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr)

#creating 2D numpy array
import NumPy as np
b = np.array([[1, 2, 3], [4, 5,6]])
print(b)

#using numpy array to perform mathematical operations
import NumPy as np
a = np.array([1, 2, 3, 4, 5])
b = np.array([6, 7, 8, 9, 10])

print(a+b)
print(a-b)
print(a*b)
print(a/b)

#slicing and indexing numpy arrays
import NumPy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr[2])


print(arr[1:3])

#reshaping numpy arrays
import NumPy as np
arr = np.array([1, 2, 3, 4, 5,6])
print(arr.reshape(2,3))