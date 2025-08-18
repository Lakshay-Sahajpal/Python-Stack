import numpy as np

arr = np.arange(1, 10)
print(arr)
print("=====================")

arr_resh = arr.reshape(3,3)#reshaping the 1d array to 3x3
print(arr_resh)
print("=====================")

arr_flat = arr_resh.flatten()#converting 2d to 1d array
print(arr_flat)

arr_flat[0] = 99
print(arr_flat)
print()

print("=====================")
arr_resh[1] = 100 #this will consider arr_resh as 2d array only and will assign 100 to 1column,1 row
print(arr_resh)
print()

print("")

arr_resh.flat[0] = 99 # this will consider arr_rash as 1d array and 
print(arr_resh)
print()

#arr_flat.flatten[2] = 101::::::This will show error as flatten do not support value assignment, we can only do it with Flat[] or after copy
# print(arr_flat)

print("=====================")

print(arr_resh)

#Indexing in Array
print(arr_resh[2,2])
print(arr_resh[-1])
print(arr_resh[1][2])
