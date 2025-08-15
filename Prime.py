
#Prime number
# -> take input an convert to int list
# -> convert to 1d array 
# -> create another array of size input_array+1 
# -> divide every element of array 1 individually by array 2 
# -> store result of those completely divisible by only 2 numbers 
# -> return the array
import numpy as np


num = input("Enter the numbers you want to check for prime numbers(seperated by comas): ")
#creating list of the inputs.

num_list = [int(n.strip()) for n in num.split(",")]

print( num_list)

#converted to arrays
arr_in = np.array(num_list)
print(arr_in, arr_in.shape)

#get max number in the list to create range for the new array for division

max_num = max(arr_in)
print(max_num)
arr_chk = np.arange(1, (max_num+2))
print(arr_chk)

prime = np.empty(0)

for i in range (len(arr_in)):
    count = 0
    
    for j in range (len(arr_chk)):
        
        if arr_in[i] % arr_chk[j] == 0:
            count+=1
            
    if count <= 2:
        prime = np.append(prime, arr_in[i])
    
        
print("Prime values are: ", prime)

#3,7,2,5,1,4
#arr_in[i] >= arr_chk[j] and 