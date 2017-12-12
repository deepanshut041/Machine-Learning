#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score,precision_score, recall_score
from sklearn.model_selection import train_test_split, cross_val_score


data_dict = pickle.load(open("../tools/final_project_dataset_unix.pkl", "rb") )

### first element is our labels, any added elements are predictor
### features. Keep this the same for the mini-project, but you'll
### have a different feature list when you do the final project.
features_list = ["poi", "salary"]

sort_keys = '../tools/python2_lesson14_keys_unix.pkl'
data = featureFormat(dictionary=data_dict, features=features_list, sort_keys=sort_keys)
labels, features = targetFeatureSplit(data)



### it's all yours from here forward!  

# Dividing data into test and traning data using sklearn
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.3, random_state=42)

clf = DecisionTreeClassifier()

clf.fit(features_train, labels_train)

pred = clf.predict(features_test)

ac_score = accuracy_score(labels_test, pred)
pr_score = precision_score(labels_test, pred)
re_score = recall_score(labels_test, pred)

print()
print()



true_positive = 0
true_negative = 0
false_negative = 0
false_positive = 0
for i,j in zip(pred, labels_test):
	if j == 1:
		if j == i:
			true_positive += 1
		else:
			false_negative += 1
	else:
		if j == i:
			true_negative += 1
		else:
			false_positive += 1


print("True Positive : ", true_positive)
print()
print("True Negative : ", true_negative)
print()
print("False Positive : ", false_positive)
print()
print("False Negative : ", false_negative)
print()
print("Accuracy of classifier tree is : ", ac_score)
print()
print("Precision of classifier tree is : ", pr_score)
print()
print("Recall of classifier tree is : ", re_score)
print()
print()
