import random
import time
import numpy as np

#method1 using list
data_list = [random.random() for _ in range(100000000)]

#calculate mean using python lists
start = time.time()
mean_list = sum(data_list)/len(data_list)
end = time.time()
print("Mean list:", mean_list)
pyl = end-start
print("Time taken: ",pyl)

#method2 using numpy
start = time.time()
mean_array = np.mean(data_list)
end = time.time()
print("Mean Numpy: ",mean_array)
npt = end - start
print("Time taken: ",npt)

#let's decide who wins
if npt < pyl:
    print("Python list is faster")
elif npt > pyl:
    print("Numpy is faster")
else:
    print("Both are equal")
