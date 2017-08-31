 """
Has it been trained with human supervision
supervised VS unsupervised VS semisupervised VS reinforcement learning.
"""
"""
Can it learn incrementaly on the fly
online VS batch learning
"""
"""
Does it work by comparing new data points to known data points or by detecting patterns in the training data amd build a predictive model.
instance-based CS model-based learning
"""
"""
Supervised Learning
Learning with given solutions calles labels
It must then learn how to classify new emails.
Important supervised learning algorithms:
-K-Nearest Neighbors
-Linear Regression
-Logistic Regression
-Support Vector Machines (SVMs)
-Decision Trees and Random Forests
-Neural networks
"""
"""
Unsupervised Learning
In unsupervised learning the training set in not labeled.
Important unsupervied learning algorithms:
-Clustering
	-k-means
	-Hierarcgucal Cluster Analysis(HCA)
	-Expectation Maximization
-Visualization and dimensionality reduction
	-Principal Component Analysis(PCA)
	-Kernal PCA
	-Locally-Linear Embedding(LLE)
	-t-distrubuting Stochastic Neighbor Emvedding(t-SNE) 
-Association rule learning
	-Apriori
	-Eclat
"""
"""
Semi-Supervised Learning
Some algorithms can deal with partially labeled training data. Mostly ublabeled and a bit of labeled data.
Most Semi-supervised learning algorithms are combinations of unsupervised abd supervised algorithms.
For example deep belief networks (DBNs) are based on usupervised components called restricted Boltzmann machines(RBMs) stacked ontop of one another.
They are trained sequetially in an unsupervised manner, and then the whole system is fine-tuned using supervised learning techniques.
"""
"""
Reinforcement Learning
The learning system, called an agent in this context, can observe the environment, select and perfor actions, and get rewards in return(or penalties in the form of negative rewards)
It then must learn by itself what is the best strategy, called a policy, to get the most reward over time.
A policy defines what action agent should choose when it is in a given situation.
"""
