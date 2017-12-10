#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
#Importing SVC from sklearn for making naive bayes classifier 
from sklearn.svm import SVC 
#Importing accuracy_score from sklearn.metrics for getting accuracy score 
from sklearn.metrics import accuracy_score
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()


#Use this lines only if you want 1% of total dataset
# features_train = features_train[0:int(len(features_train)/100)] 
# labels_train = labels_train[0:int(len(labels_train)/100)]


#This is t0 time counter for trannig classifier
t0 = time()
#########################################################
### Classifier code  goes here ###

#Made classifier
clf  = SVC(kernel="rbf", C=10000)

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
k = 0
for i in range(0, len(pred), 1):
	if pred[i] == 1:
		k = k + 1

#printing accuracy score
print()
print("Accuracy is : ",score)
print()
print("Chris(1) emails are : ",k)
print()
print("Sara(0) emails are : ",len(pred) - k)
print()
print()

#########################################################


