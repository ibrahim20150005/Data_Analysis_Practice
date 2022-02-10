#!/usr/bin/env python
# coding: utf-8

# # **K-Means Clustering with Python Scikit Learn**

# ## **Prediction Using Unsupervised ML**
# ● From the given ‘Iris’ dataset, predict the optimum number of clusters and represent it visually.

# ### Author: Ibrahim Ahmed Saber.

# ### 1- Import Libraries

# In[1]:


#Importing all libraries
import pandas as pd
import numpy as np
import  matplotlib.pyplot as plt  
from sklearn.cluster import KMeans
get_ipython().run_line_magic('matplotlib', 'inline')


# ### 2- Load Reading

# In[2]:


from sklearn import datasets

# Load the iris dataset
iris = datasets.load_iris()
iris_df = pd.DataFrame(iris.data, columns = iris.feature_names)
# Species ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
iris_df.head()


# ### 3- Elbow Plot

# >#### Here we will find the optimum number of clusters for K Means

# In[3]:


# Finding the optimum number of clusters for k-means classification
plt.figure(figsize=(12, 10), dpi=60)

x = iris_df.iloc[:,[0,1,2,3]].values

sse = []
k_range = range(1,10)
for k in k_range:
    km = KMeans(n_clusters=k,random_state=0)
    km.fit(x)
    sse.append(km.inertia_)

plt.xlabel('K')
plt.ylabel('Sum Of Squared Error')
plt.plot(k_range,sse)
plt.show()


# >#### From this we choose the number of clusters as "**3**".

# ### 4-  Visualising the Dataset before the clusters 

# In[4]:


# On the first two columns
plt.figure(figsize=(12, 10), dpi=60)

plt.scatter(iris_df.iloc[:,[0]].values,iris_df.iloc[:,[1]].values)
plt.xlabel('Length (cm)')
plt.ylabel('Width (cm)')
plt.show()


# ### 5- Applying k-means

# >#### Applying k-means to the dataset / Creating the k-means classifier

# In[5]:


km = KMeans(n_clusters = 3,random_state = 0)
y_predicted = km.fit_predict(x)


# In[6]:


# Visualising the clusters - On the first two columns
plt.figure(figsize=(12, 10), dpi=60)

plt.scatter(x[y_predicted == 0, 0], x[y_predicted == 0, 1], 
            s = 100, c = 'red', label = 'Iris-setosa')
plt.scatter(x[y_predicted == 1, 0], x[y_predicted == 1, 1], 
            s = 100, c = 'blue', label = 'Iris-versicolour')
plt.scatter(x[y_predicted == 2, 0], x[y_predicted == 2, 1],
            s = 100, c = 'green', label = 'Iris-virginica')

# Plotting the centroids of the clusters
plt.scatter(km.cluster_centers_[:, 0], km.cluster_centers_[:,1], 
            s = 100, c = 'yellow', label = 'Centroids')


plt.legend()
plt.show()


# ### Thank You
