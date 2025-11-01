import numpy as np

#create 1D array list using built in method
data_list = [1,2,3,4,5,6]

#reshape into 2x3 matrix
data_matrix = [data_list[i:i +3] for i in range(0,len(data_list),3)]
print(data_matrix)

#Transpose the "Matrix"
transposed_matrix = [[data_matrix[j][i] for j in range(len(data_matrix))] for i in range(len(data_matrix[0]))]
print("Transposed list (3x2):")
print(transposed_matrix)

#using numpy method
#create 1D array
data_array = np.array([1,2,3,4,5,6])

reshaped_array = data_array.reshape(2,3)
print(reshaped_array)

#transpose this martrix
transposed_array = reshaped_array.T
print(transposed_array)
