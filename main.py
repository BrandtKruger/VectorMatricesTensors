import sys
import numpy as np

# define a scalar
x = 6
print("Scalar is ",  x)

# define a vector
y = np.array((1,2,3))
print("Vector \n", y)
print("Vector dimension: {}".format(y.shape))
print("Vector size: {}".format(y.size))

# define matrix
z = np.matrix([[1,2,3], [4, 5, 6], [7, 8, 9]])
print("Matrix \n", z)
print("Matrix dimension: {}".format(z.shape))
print("Matrix size: {}".format(z.size))

# define a matrix of a given dimension
a = np.ones((4, 4))
print("Matrix by dimension 4 x 4\n", a)
print("Matrix dimension: {}".format(a.shape))
print("Matrix size: {}".format(a.size))

# Tensor
b = np.zeros((3, 3, 3, 3))
print("Matrix by dimension 3 x 3 X 3 X 3\n", b)
print("Matrix dimension: {}".format(b.shape))
print("Matrix size: {}".format(b.size))

# Declare by index
c = np.ones((5, 5), dtype = np.int)
print("Matrix by index 5 X 5\n", c)
print("Matrix dimension: {}".format(c.shape))
print("Matrix size: {}".format(c.size))

# Set Row 0 Column 1 to value 2
c[0, 1] = 2
print("Set Row 0 Column 1 to value 2\n", c)

# Set All Rows Column 0 to value 3
c[:,0] = 3
print("Set All Rows Column 0 to value 3\n", c)

# Set All Rows and Columns to value 5
c[:,:] = 5
print("Set All Rows and Columns to value 5\n", c)

# For higher dimensions add a index
d = np.ones((5, 5, 5), dtype=np.int)
# Assign the first row a new value
d[:,0,0] = 6
print("Higher dimension\n", d)

# Matrix add operation
e = np.matrix([[1,2], [3,4]])
f = np.mat([[5,6],[7,8]])
print( "\nMatrix e is \n", e ,"\nMatix f is\n", f)
g = e + f
print("\nSum of matrix e and f is\n", g)

# Matrix subtracting operation
print( "\nMatrix e is \n", e ,"\nMatix f is\n", f)
h = e - f
print("\nSubtraction of matrix e and f is\n", h)

# Matrix multiplication operation
print( "\nMatrix e is \n", e ,"\nMatix f is\n", f)
i = e * f
print("\nMultiplication of matrix e and f is\n", i)

# Matrix transpose
j = np.array(range(9))
j = j.reshape(3,3)
print("\nBefore transpose\n", j)
k = j.T
print("\nAfter transpose\n", k)

# Tensors
l = np.ones((3,3,3,3,3,3,3,3,3,3))
print("Tensors\n", l)
print("\nShape\n", l.shape)
# print("\nLen\n", l.len)
print("\nSize\n", l.size)


