import numpy as np

array = np.array([[1, 2, 3], [4, 5, 6]])
print(array)
# print(type(array))
print(array.shape)


array2 = np.zeros((3, 4), dtype=int)
array2 = np.ones((3, 4), dtype=int)
array2 = np.full((3, 4), 5, dtype=int)
array2 = np.random.random((3, 4))
print(array2)
# print(array2[0, 0])
# print(array2 > 0.2)
# print(array2[array2 > 0.2])
# print(np.sum(array2))
# print(np.floor(array2))
# print(np.ceil(array2))
# print(np.round(array2))

first = np.array([1, 2, 3])
second = np.array([1, 2, 3])

# print(first + 2)
# print(first + second)

# pure python

dimensions_inch = [1, 2, 3]
dimensions_cm = [x * 2.54 for x in dimensions_inch]
print(dimensions_cm)

# numpy
dimensions_inch = np.array([1, 2, 3])
dimensions_cm = dimensions_inch * 2.54

print(dimensions_cm)
