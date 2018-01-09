import numpy as np

a = [i for i in range(9)]
a = np.array(a)
print(a)
a = a.reshape((1, 9))
print(a)
a = a.reshape((3, 3))
print(a)
a = a.reshape((3, 1, 3))
print(a)
a = a.reshape((9, 1))
print(a)
a = a.reshape((3, 3))
print(a)