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

