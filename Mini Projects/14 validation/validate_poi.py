#!/usr/bin/python


"""
    Starter code for the validation mini-project.
    The first step toward building your POI identifier!

    Start by loading/formatting the data

    After that, it's not our code anymore--it's yours!
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split, cross_val_score


data_dict = pickle.load(open("../tools/final_project_dataset_unix.pkl", "rb") )

### first element is our labels, any added elements are predictor
### features. Keep this the same for the mini-project, but you'll
### have a different feature list when you do the final project.
features_list = ["poi", "salary"]

sort_keys = '../tools/python2_lesson13_keys_unix.pkl'
data = featureFormat(dictionary=data_dict, features=features_list, sort_keys=sort_keys)
labels, features = targetFeatureSplit(data)



### it's all yours from here forward!  

# Dividing data into test and traning data using sklearn
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.3, random_state=42)

clf = DecisionTreeClassifier()

clf.fit(features_train, labels_train)

pred = clf.predict(features_test)

score = accuracy_score(labels_test, pred)

print("Accuracy of classifier tree is : ", score)
