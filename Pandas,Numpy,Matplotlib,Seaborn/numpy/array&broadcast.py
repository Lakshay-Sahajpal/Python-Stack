import numpy as np


data = [1, 3, 5, 7, 8]
arr1 = np.array(data)
print(arr1, type(arr1))
print(arr1.dtype)


arr2 = np.array([[2,4,6],[8,3,7],[0,8,5]])
print(arr2, type(arr2))
print(arr2.dtype)

print(arr2.shape, arr1.shape) #it will return the rows and colums f the array row, column

print(arr2.size, arr1.size) #it will give the total items present in the array

print(arr2.ndim, arr1.ndim) #it will give the dimention of the array(1d, 2d, 3d etc)

arr_x = np. array([1, 4, 6])
arr_y = np. array([4, 46, 68])

arr_new = arr_x + arr_y
print(arr_new) #Operators in array

arr_x = np. array([[1,4,6], [4,8,2]])
arr_y = np. array([[4,46], [6,8], [7,3]])

#print(arr_x + arr_y):::Here broadcasting is not possible, so it will create error and will not add

