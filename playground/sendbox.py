import numpy as np

# a = [i for i in range(9)]
# a = np.array(a)
# print(a)
# a = a.reshape((1, 9))
# print(a)
# a = a.reshape((3, 3))
# print(a)
# a = a.reshape((3, 1, 3))
# print(a)
# a = a.reshape((9, 1))
# print(a)
# a = a.reshape((3, 3))
# print(a)

a = [i for i in range(24)]
b = [i for i in range(12)]

a = np.array(a)
b = np.array(b)
a = a.reshape((2, 3, 4))
b = b.reshape((4, 3))


print(a.shape)
print(b.shape)
c = np.matmul(a, b)
print(c.shape)
print(a)
print(b)
print(c)