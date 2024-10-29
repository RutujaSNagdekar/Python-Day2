import numpy as np

a = np.array([1,2,3,4,5,6])
print(a.dtype)
print(a)

b = np.array([[1,2,3,4,5,6],[7,8,9,10,11,12]])
print(b)

c = np.array([[[1,2,3,4,5,6], [7,8,9,10,11,12], [13,14,15,16,17,18]]])
print(c)
print(type(a))

z = a+b
print(z)

print(a.size)
print(b.size)
print(c.size)

print(a.shape)
print(b.shape)
print(c.shape)

print(a.dtype)
print(b.dtype)
print(c.dtype)


d = np.array([
    [1,2,3,4,5.5,6],
    [7,8,9,10,11,12]
])

print(d.dtype)

d = np.array([[1, 2, 3, 4, 5.5, 6], [7, 8, 9, 10, 11, 12]])

print(d)
print(d.transpose())
x = np.zeros(8)
print(x)

x = np.zeros((4,8), dtype=str)
print(x)

x = np.zeros((4,8), dtype=bool)
print(x)

x = np.zeros((4, 8), dtype=int)
print(x)

x = np.ones(8)   ### To generate 8 columns of array (default float data type)
print(x)
a = np.arange(1, 20,2)
print(a)