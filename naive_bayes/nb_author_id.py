#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project. 

    Use a Naive Bayes Classifier to identify emails by their authors
    
    authors and labels:
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
    ### import the sklearn module for GaussianNB
    from sklearn.naive_bayes import GaussianNB

    ### create classifier
    clf = GaussianNB()

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

    ### calculate and return the accuracy on the test data
    from sklearn.metrics import accuracy_score
    accuracy = accuracy_score(pred, labels_test)
    
    ### Another way
    ### accuracy = clf.score(features_test, labels_test)
    return accuracy

print NBAccuracy(features_train, labels_train, features_test, labels_test)
#########################################################

### Your exact results for time may vary, 
### but we found that predicting with this particular 
### setup takes about 30x less time than training.

#no. of Chris training emails: 7936
#no. of Sara training emails: 7884
#Training time: 1.299 s
#Prediction time: 0.199 s
#0.973265073948
