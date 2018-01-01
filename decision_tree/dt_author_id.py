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
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
def NBAccuracy(features_train, labels_train, features_test, labels_test):
    """ compute the accuracy of your Naive Bayes classifier """
    ### import the sklearn module for decision tree
    from sklearn import tree

    print "Number of features in train data:", len(features_train[0])
    print "Number of features in test data:", len(features_test[0])
    ### create classifier tune it with min_samples_split=2
    clf = tree.DecisionTreeClassifier(min_samples_split=40)

    ### Calculate the Time spent to train our algorithm
    t0 = time()
    ### fit the classifier on the training features and labels
    clf.fit(features_train, labels_train)
    print "Training time:", round(time()-t0, 3), "s"

    ### Calculate the Time spent in the prediction
    t0 = time()
    ### use the trained classifier to predict labels for the test features
    pred = clf.predict(features_test)

    print "Prediction time:", round(time()-t0, 3), "s"

    #print "Prediction for element #10:", pred[10]
    #print "Prediction for element #26:", pred[26]
    #print "Prediction for element #50:", pred[50]
    #print "We could predict ", (sum(i == 1 for i in pred)),"in ", len(features_test),"test events bilong to Chris"

    ### calculate and return the accuracy on the test data
    from sklearn.metrics import accuracy_score
    accuracy = accuracy_score(pred, labels_test)
    
    ### Another way
    ### accuracy = clf.score(features_test, labels_test)
    return accuracy

print NBAccuracy(features_train, labels_train, features_test, labels_test)


#########################################################


# Training time: 65.297 s
# Prediction time: 0.026 s
# 0.9795221843

# {'acc_min_samples_split_50': 0.912, 'acc_min_samples_split_2': 0.908}