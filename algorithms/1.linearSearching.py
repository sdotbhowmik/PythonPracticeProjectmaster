def linearSearch(my_array, key):
    for i in range(len(my_array)):
        if my_array[i] == key:
            return "key found in possition: ", i+1 #index =1, possition = index+1 which menas i+1
    return 'Not found'

### Test 1 ###
print(linearSearch([1, 5, 10, 12, 25, 30, 32], 29))

### Test 2 ###
print(linearSearch([5, 10, 15, 20, 25], 15))