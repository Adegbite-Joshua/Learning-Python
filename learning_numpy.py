import numpy as np

a = np.array([0,1,2,3,4,5])
a = np.array([0,1,2,3,4,5], dtype='<U1')

# x = lambda a, b : a + b
# print(x(2,3))


print(a[1])
print(a[:3])
print(a[2:])
print(type(a))
print(type(a[1]))

# python.exe -m pip install --upgrade pip