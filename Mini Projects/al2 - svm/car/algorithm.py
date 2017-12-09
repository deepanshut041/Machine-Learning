#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture
#Importing SVC from sklearn for making naive bayes classifier 
from sklearn.svm import SVC 
#Importing accuracy_score from sklearn.metrics for getting accuracy score 
from sklearn.metrics import accuracy_score
from time import time

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
plt.show()
################################################################################


### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary
#This is t0 time counter for trannig classifier
t0 = time()
#########################################################
### Classifier code  goes here ###

#Made classifier
clf  = SVC()

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

#########################################################


try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass
