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
# print(x_values)

x_values = np.linspace(0,100,5)
x_values2 = np.linspace(0,1000,5)
# print(x_values)
# print(x_values2)

l1 = [1,2,3,4,5]
l2 = [6,7,8,9,0]

a1 = np.array([1,2,3,4,5])
a2 = np.array([6,7,8,9,0])

# print(l1 + l2)
# print(a1 + a2)
# print(a1 * a2)
# print(a1 % a2)
# print(a1 - a2)

# print(np.append(a1, ['a','b', 'c']))
# a1 = np.append(a1, ['a','b', 'c'])
# print(a1)

a = np.array([[1,2,3,4,5],
              [6,7,8,9,10],
              [11,12,13,14,15],
              [16,17,18,19,20]])

# print(a.shape)
# # print(a.reshape((5,2,1,1,2)))
# a.reshape((5,2,1,1,2))
# print(a)

# a.resize((5,2,1,1,2))
# print(a)

# print(a.flatten())

# var1 = a.ravel()
# var1[1] = 100

# print(var1)
# print(a)

# number = np.random.randint(95,100)
# numbers = np.random.randint(95,100, size=(2,3,4))

# print(number)

# np.save('myarray.npy', a)
# a = np.load('myarray.npy')
# print(a)


# np.savetxt('myarray.csv', a, delimiter=',')
a = np.loadtxt('myarray.csv', delimiter=',', dtype='<U11')

print(a)