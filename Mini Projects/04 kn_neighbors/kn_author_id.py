#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
#Importing KNeighborsClassifier from sklearn for making K Nearest Neighbor classifier 
from sklearn.neighbors import KNeighborsClassifier 
#Importing accuracy_score from sklearn.metrics for getting accuracy score 
from sklearn.metrics import accuracy_score
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

#This code here only decrease number of testing data
# features_test = features_test[:int(len(features_test)/10)]
# labels_test = labels_test[:int(len(labels_test)/10)]

#This is t0 time counter for trannig classifier
t0 = time()
#########################################################
### Classifier code  goes here ###

#Made classifier
clf  = KNeighborsClassifier(n_neighbors=1, algorithm='brute')

#Now fitting classifier on traning data
#Note: Fitting here means tranning classifier on data
clf.fit(features_train, labels_train)


#Printing here training time classifer takes
print("training time:", round(time()-t0, 3), "s")


#Now prediciting using classifier
#Note: Always call classifier after fitting data

#t1 is time for doing predictions
t1 = time()

pred = clf.predict(features_test)

#Printing here predecting time classifer takes
print("predecting time:", round(time()-t1, 3), "s")


#Now testing the accuracy of classifier
#For Accuracy iam using sk_learn accuracy_score function 
score =  accuracy_score(labels_test, pred)


#printing accuracy score
print()
print("Accuracy is : ",score)
print()
print()

#########################################################


