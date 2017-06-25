'''

Title: Machine Learning Recipe 1
Purpose: 
Program : ML.py
Author: Archana Raghu

'''
#importing modules
from sklearn import tree

#features and labels
features = [[140, 1], [130, 1], [150, 0], [170, 0]]
labels = [0, 0, 1, 1]

#creating classifiers
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)


print (clf.predict([[150, 0]]))


