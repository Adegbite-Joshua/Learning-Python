import numpy as np

# a = np.array([0,1,2,3,4,5])
# a = np.array([0,1,2,3,4,5], dtype='<U1')

# x = lambda a, b : a + b
# print(x(2,3))


# print(a[1])
# print(a[:3])
# print(a[2:])
# print(type(a))
# print(type(a[1]))


# a_multidimension = np.array([[1,2,3,4,5],
#                              [6,7,8,9,0],
#                              ])

# a_multidimension = np.array([[1,2,3,4,5],
#                              [6,7,8,9,0],
#                              [1,1,1,1, 'h']
#                              ])

# print(a_multidimension.shape)
# print(a_multidimension.size)
# print(a_multidimension.ndim)

# print(a_multidimension.dtype)

# Indexing the numpy arrays
# print(a_multidimension[1, 4])
# print(a_multidimension[1][4])


# Creating auto filled numpy arrays
a =  np.full((3,3,3), 9)
b=  np.full((3,3,3), 1)
zeros = np.zeros((3,3,3))
ones = np.ones((3,3,3))
empty = np.empty((4,4,4))

# print(a)
# print(b)
# print(zeros)
# print(ones)
# print(empty)

x_values = np.arange(0,100,4)
print(x_values)

x_values = np.linspace(0,100,5)
x_values2 = np.linspace(0,1000,5)
print(x_values)
print(x_values2)