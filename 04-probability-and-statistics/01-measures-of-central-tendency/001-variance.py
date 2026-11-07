import numpy as np

x = [2, 4, 4, 4, 6]

print("Mean:", np.mean(x))
print("Population variance:", np.var(x))

mean = (sum(x)/len(x))
deviations = [element - mean for element in x]
squared_deviations = [element**2 for element in deviations]
variance = sum(squared_deviations)/len(deviations)

print(mean)
print(deviations)
print(squared_deviations)
print(variance)

x_vec = np.array([2, 4, 4, 4, 6])

mean = np.mean(x_vec)
deviations = x_vec - mean
squared_deviations = deviations ** 2
variance = np.mean(squared_deviations)

A = np.array([2, 4, 4, 4, 6])
C = 3 * A

var_A = np.mean((A - np.mean(A)) ** 2)
var_C = np.mean((C - np.mean(C)) ** 2)

print("Variance A:", var_A)
print("Variance C:", var_C)
print("Variance ratio:", var_C / var_A)

#Using NumPy, write a short Python program that:
## Creates an array x containing [2, 4, 4, 4, 6].
x_vec = np.array([2, 4, 4, 4, 6])
## Creates a transformed array y = 2*x - 3.
x_vec_trans = x_vec*2 - 3
## Prints the mean and population variance of both arrays.
print(np.mean(x_vec))
print(np.mean(x_vec_trans))
print(np.var(x_vec))
print(np.var(x_vec_trans))
## Checks whether the results match our predictions.