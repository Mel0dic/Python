import numpy as np
import matplotlib.pyplot as plt

#Create an array containg any number of zeros
#  in this case 5
np.zeros(5)

#You can also use this to create a multidimensional array
# here it us 3x4
np.zeros((3,4))


#Set a to a 2d array
a = np.zeros((3,4))

#To get the shape use .shape
a.shape

#.ndim is equal to len(a.shape) which is equal to the rank? / dimensions
a.ndim

#for the size of the array
a.size

 

#Creating N dimensional arrays

#Here is a 3d array
np.zeros((2,3,4))


#Numpy arrays have the type ndarrays (n-dimensional)
type(np.zeros((3,4)))

#Many other NumPy arrays create ndarrays
# for example to get an array of 1s use...
np.ones((3,4))

# or to get an array filled with a given value use...
np.full((3,4), np.pi)

# you can also make an uninitialised array which has an unpredictable content
# it uses whatever is in memory at that point
np.empty((2,3))

# you can also use the regular python way by calling
np.array([[1,2,3,4], [5,6,7,8]])

#to create an array with a range of numbers use
np.arange(1,5)

#this also works with floats
np.arange(1.0, 5.0)

#you can add a step peramete to this also
np.arange(1.0, 5.0, 0.5)

#BUT when dealing with floats it is not easy to predict the exact number of
#elements in the array
#depending on floating point errors, the max value is 4/3 or 5/3.
np.arange(0, 5/3, 1/3)
np.arange(0, 5/3, 0.333333333)
np.arange(0, 5/3, 0.333333334)
#which means sometimes .linspace() is better use when using floats
np.linspace(0,5/3, 6)


#A number of functions are available in NumPy's random module to create ndarrays 
#initialized with random values. For example, here is a 3x4 matrix initialized 
#with random floats between 0 and 1
np.random.rand(3,4)

#Here's a 3x4 matrix containing random floats sampled from a univariate normal 
#distribution (Gaussian distribution) of mean 0 and variance 1:
np.random.randn(3,4)

plt.hist(np.random.rand(100000), normed=True, bins=100, histtype="step", color="blue", label="rand")
plt.hist(np.random.randn(100000), normed=True, bins=100, histtype="step", color="red", label="randn")
plt.axis([-2.5, 2.5, 0, 1.1])
plt.legend(loc = "upper left")
plt.title("Random distributions")
plt.xlabel("Value")
plt.ylabel("Density")
plt.show()

#initialize an ndarray using a function
def my_function(z, y, x):
	return x * y + z
#print(np.fromfunction(my_function, (3, 2, 10)))

#NumPy's ndarrays are also efficient in part because all their 
#elements must have the same type (usually numbers). You can check 
#what the data type is by looking at the dtype attribute:

c = np.arange(1, 5)
print(c.dtype, c)

c = np.arange(1.0, 5.0)
print(c.dtype, c)

#Instead of letting NumPy guess what data type to use, you can set it
#explicitly when creating an array by setting the dtype parameter:
d = np.arange(1, 5, dtype=np.complex64)
print(d.dtype, d)


#The itemsize attribute returns the size (in bytes) of each item
e = np.arange(1, 5, dtype=np.complex64)
print(e.itemsize)

#An array's dat is stored as a flat (one dimensional) byte buffer.
#It is available via the data attribute (you will rarely need it
#though)
f = np.array([[1,2], [1000, 2000]], dtype=np.int32)
print(f.data)

#In python 2, f.data is a buffer. In python 3, it is a memoryview.
if (hasattr(f.data, "tobytes")):
    data_bytes = f.data.tobytes() # python 3
else:
    data_bytes = memoryview(f.data).tobytes() # python 2

print(data_bytes)

#Several ndarrays can share the same data buffer, meaning that 
#modifying one will also modify the others. We will see an example
#in a minute.

#RESHAPING AN ARRAY

#changing an array of an ndarray is as simple as setting its shape
#attribute. However, the array's size must remain the same.

print('\n\n\n')

g = np.arange(24)
print(g)
print("Rank:", g.ndim)

g.shape = (6, 4)
print(g)
print("Rank:", g.ndim)

g.shape = (2, 3, 4)
print(g)
print("Rank:", g.ndim)


#RESHAPE

#The reshape function returns a new ndarray object pointing 
#at the same data. This means that modifying one array will 
#also modify the other.

print("\n\n\n")
g2 = g.reshape(4,6)
print(g2)
print("Rank:", g2.ndim)

#Set item at row 1, col 2 to 999 (more about indexing below).
g2[1, 2] = 999
print(g2)

#This modifies the corresponding element in g
print(g)

#Finally, the ravel function returns a new one-dimensional ndarray
#that also points to the same data
print(g.ravel()) 


#ARITHMETIC OPERATIONS

#All the usual arithmetic operators (+, -, *, /, //, **, etc.) 
#can be used with ndarrays. They apply elementwise:
a = np.array([14, 23, 32, 41])
b = np.array([5,  4,  3,  2])
print("a + b  =", a + b)
print("a - b  =", a - b)
print("a * b  =", a * b)
print("a / b  =", a / b)
print("a // b  =", a // b)
print("a % b  =", a % b)
print("a ** b =", a ** b)

#Broadcasting