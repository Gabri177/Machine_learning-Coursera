import numpy as np
import time

# Vector creation

a1 = np.zeros(4)
a2 = np.zeros((4,))
a3 = np.random.random_sample(4)
print(f"a1 = {a1}\na2 = {a2}\na3 = {a3}")

# Generate an int array of interval between 0 and 4, 0 is included but 4 no.
a4 = np.arange(4.)
a5 = np.random.rand(4)
print(f"a4 = {a4}\na5 = {a5}\n")

# Generate different type of array through numpy
a6 = np.array([5, 4, 3, 2])
a7 = np.array([5., 4, 3, 2])
print(f"a6 = {a6}\na7 = {a7}\n")

# vector indexing operations on 1-D vectors
a = np.arange(10)
print (a)

# access an element
print (a[:2])
print (a[1:])

try:
    c = a[10]
except Exception as e:
    print("The error message you'll see is:")
    print(e)



# Slicing

# access 5 consecutive elements (start:stop:step)
c = a[2:7:1];     print("a[2:7:1] = ", c)

# access 3 elements separated by two
c = a[2:7:2];     print("a[2:7:2] = ", c)

# access all elements index 3 and above
c = a[3:];        print("a[3:]    = ", c)

# access all elements below index 3
c = a[:3];        print("a[:3]    = ", c)

# access all elements
c = a[:];         print("a[:]     = ", c)



# Single vector operations

a = np.array([1,2,3,4])
print(f"a             : {a}")

# negate elements of a
b = -a
print(f"b = -a        : {b}")

# sum all elements of a, returns a scalar
b = np.sum(a)
print(f"b = np.sum(a) : {b}")

b = np.mean(a)
print(f"b = np.mean(a): {b}")

b = a**2
print(f"b = a**2      : {b}")



# Vector Vector element-wise operations

a = np.array([ 1, 2, 3, 4])
b = np.array([-1,-2, 3, 4])
# for this to work correctly, the vectors must be of the same size
print(f"Binary operators work element wise: {a + b}")



# Scalar Vector operations

a = np.array([1, 2, 3, 4])
b = 5 * a
print(f"b = 5 * a : {b}")



# Vector Vector dot product

def my_dot(a ,b):
    # compute the dot product of two vectors
    x = 0
    for i in range(a.shape[0]):
        x += a[i] * b[i]
    return x
# test 1-D
a = np.array([1, 2, 3, 4])
b = np.array([-1, 4, 3, 2])
print(f"my_dot(a, b) = {my_dot(a, b)}")
# test 1-D
a = np.array([1, 2, 3, 4])
b = np.array([-1, 4, 3, 2])
c = np.dot(a, b)
print(f"NumPy 1-D np.dot(a, b) = {c}, np.dot(a, b).shape = {c.shape} ")
c = np.dot(b, a)
print(f"NumPy 1-D np.dot(b, a) = {c}, np.dot(a, b).shape = {c.shape} ")



# show common Course 1 example
X = np.array([[1],[2],[3],[4]])
w = np.array([2])
c = np.dot(X[1], w)

print(f"X[1] has shape {X[1].shape}")
print(f"w has shape {w.shape}")
print(f"c has shape {c.shape}")



# Matrices

#  Matrices Creation
a = np.zeros((1, 5))
print(f"a shape = {a.shape}, a = \n{a}")

a = np.zeros((2, 1))
print(f"a shape = {a.shape}, a = \n{a}")

a = np.random.random_sample((1, 1))
print(f"a shape = {a.shape}, a = \n{a}")

# NumPy routines which allocate memory and fill with user specified values
a = np.array([[5], [4], [3]]);   print(f" a shape = {a.shape}, np.array: a = {a}")
a = np.array([[5],   # One can also
              [4],   # separate values
              [3]]); #into separate rows
print(f" a shape = {a.shape}, np.array: a = {a}\n\n\n")



# Operations on Matrices

#vector indexing operations on matrices
a = np.arange(6).reshape(-1, 2)   #reshape is a convenient way to create matrices
print(f"a.shape: {a.shape}, \na= {a}")

#access an element
print(f"\na[2,0].shape:   {a[2, 0].shape}, a[2,0] = {a[2, 0]},     type(a[2,0]) = {type(a[2, 0])} Accessing an element returns a scalar\n")

#access a row
print(f"a[2].shape:   {a[2].shape}, a[2]   = {a[2]}, type(a[2])   = {type(a[2])}")

# Slicing

#vector 2-D slicing operations
a = np.arange(20).reshape(-1, 10)
print(f"a = \n{a}")

#access 5 consecutive elements (start:stop:step)
print("a[0, 2:7:1] = ", a[0, 2:7:1], ",  a[0, 2:7:1].shape =", a[0, 2:7:1].shape, "a 1-D array")

#access 5 consecutive elements (start:stop:step) in two rows
print("a[:, 2:7:1] = \n", a[:, 2:7:1], ",  a[:, 2:7:1].shape =", a[:, 2:7:1].shape, "a 2-D array")

# access all elements
print("a[:,:] = \n", a[:,:], ",  a[:,:].shape =", a[:,:].shape)

# access all elements in one row (very common usage)
print("a[1,:] = ", a[1,:], ",  a[1,:].shape =", a[1,:].shape, "a 1-D array")
# same as
print("a[1]   = ", a[1],   ",  a[1].shape   =", a[1].shape, "a 1-D array")
