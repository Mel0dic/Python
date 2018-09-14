import pandas as pd #Pandas used to work with data as tables
import numpy as np #Help using number matrices
import matplotlib.pyplot as plt #To print the data on a graph or table
import tensorflow as tf #Google tensorflow

#Step 1 - load data
# Read the data as a dataframe object
dataframe = pd.read_csv('./data.csv')
#Use drop to get rid of unused columns. Only uising the first axis in the data set
dataframe = dataframe.drop(['index', 'price', 'sq_price'], axis=1)
#We only want the first 10 rows of the data set
dataframe = dataframe[0:10]

#Step 2 - add labels
#1 is a good buy and 0 is a bad buy
dataframe.loc[:, ('y1')] = [1,1,1,0,0,1,0,1,1,1]
#y2 is the opposite of y1, negation
dataframe.loc[:, ('y2')] = dataframe['y1'] == 0
#Turn true or false values to 1 or 0
dataframe.loc[:, ('y2')] = dataframe['y2'].astype(int)

#Step 3 - prepare data for tensorflow (tensors)
#tensors are a generic version of vectors and matrices
#Vector - is a list of number (1D tensor)
#matrix is a list od a list of numbers(2D tensor)
#list of list of lists of numbers (3D tensor)
#...
#Convert features to input tensor
inputX = dataframe.loc[:, ['area', 'bathrooms']].values
#convert labels to input tensors
inputY = dataframe.loc[:, ['y1', 'y2']].values

#Step 4 - Write out our hyperparameters
learning_rate = 0.000001
training_epochs = 2000
display_step = 50
n_samples = inputY.size

#Step 5 - Create our computation graph/ neural network
#for feature input tensors, none means any numbers of examples
#placeholders are gateways for data into our computation graph
#2 because we have 2 features. 2D matrix
x = tf.placeholder(tf.float32, [None, 2])

#Create weights
#2x2 float matrix, that we will keep updating throught the training process
#variables in tf hold and update parameters
#in memory buffers containing tensors
W = tf.Variable(tf.zeros([2,2]))

#add biases 2 because we have 2 inputs (examble is b in y = mx + b, b is the bias)
b = tf.Variable(tf.zeros([2]))

#multiply our weights by our inputs, first calculation
#weights are how wer goven how data flows in our computation graph
#matmul is matrix multiplication featur in tf
#multiply input by weights and add biases
y_values = tf.add(tf.matmul(x, W), b)

#apply softmax to value we just creates
#softmax is out activation function
y = tf.nn.softmax(y_values)

#Feed in a matrix of labels
y_ = tf.placeholder(tf.float32, [None, 2])

#Step 6 - perform training
#create our cost function, mean squared error
#reduce sum computes the sum of elements across dimensions of a tensor
cost = tf.reduce_sum(tf.pow(y_-y, 2))/(2*n_samples)

#Gradients descent
optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)

#Initialize variables and tensorflow session
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

#Training loop
for i in range(training_epochs):
	sess.run(optimizer, feed_dict={x: inputX, y_: inputY})

	#Write out logs of training
	if (i) % display_step == 0:
		cc = sess.run(cost, feed_dict={x: inputX, y_: inputY})
		print("Training step:", '%04d' % (i), "cost=", "{:.9f}".format(cc)) #, \"W=", sess.run(W), "b=", sess.run(b)

print("Optimization Finished!")
training_cost = sess.run(cost, feed_dict={x: inputX, y_: inputY})
print("Training cost=", training_cost, "W=", sess.run(W), "b=", sess.run(b), '\n')

#Its saying all houses are a good buy 7/10
#To improve add a hiden layer
print(sess.run(y, feed_dict={x: inputX}))