import numpy as np
from numpy.random import Generator as gen
from numpy.random import PCG64 as pcg
#Random number generation using PCG

np.set_printoptions(precision=3)

rand_arr = gen(pcg())
print(rand_arr.normal(size = (5,5)))#it will generate random number every time ve run the code and with NORMAL we are getting bell curve

print("===============================================================")

rand_arr = gen(pcg(seed = 100))#with setting seed it will generate randome no for every value of seed and return the same whenever it will run 
print(rand_arr.normal(size = (5,5)))

print("===============================================================")

rand_arr = gen(pcg(seed = 100))#with setting seed it will generate randome no for every value of seed and return the same whenever it will run 
print(rand_arr.integers(low = 5, high = 10, size = (5, 5)))
print("===============================================================")

rand_arr = gen(pcg())#with setting seed it will generate randome no for every value of seed and return the same whenever it will run 
print(rand_arr.integers(low = 1, high = 7))