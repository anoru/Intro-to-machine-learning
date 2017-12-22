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
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

#########################################################

def NBAccuracy(features_train, labels_train, features_test, labels_test):
    """ compute the accuracy of your Naive Bayes classifier """
    ### import the sklearn module for SVM
    from sklearn.svm import SVC

    ### create classifier specifying the kernel
    clf = SVC(kernel="rbf", C = 10000)

    ### these lines effectively slice the training dataset down 
    ### to 1% of its original size, tossing out 99% of the training data.
    #features_train = features_train[:len(features_train)/100] 
    #labels_train = labels_train[:len(labels_train)/100]

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

    print "Prediction for element #10:", pred[10]
    print "Prediction for element #26:", pred[26]
    print "Prediction for element #50:", pred[50]
    print "We could predict ", (sum(i == 1 for i in pred)),"in ", len(features_test),"test events bilong to Chris"

    ### calculate and return the accuracy on the test data
    from sklearn.metrics import accuracy_score
    accuracy = accuracy_score(pred, labels_test)
    
    ### Another way
    ### accuracy = clf.score(features_test, labels_test)
    return accuracy

print NBAccuracy(features_train, labels_train, features_test, labels_test)
#########################################################

### Exact times may vary a bit, but in general, the SVM 
### is MUCH slower to train and use for predicting than Naive bayse

### Kernel = "linear"

### training in big dataset
#no. of Chris training emails: 7936
#no. of Sara training emails: 7884
#Training time: 181.621 s
#Prediction time: 18.975 s
#0.984072810011

### smaller training dataset
#Training time: 0.102 s
#Prediction time: 1.188 s
#0.884527872582


### Kernel = "rbf"

#Training time: 0.115 s
#Prediction time: 1.241 s
#0.616040955631

# for C = 10
#0.616040955631
# for C = 100
#0.616040955631
# for C = 1000
#0.821387940842
# for C = 10000
#0.892491467577

# larger data set with rbf and C = 10000
#0.990898748578
#########################################################
