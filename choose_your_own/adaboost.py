#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture
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


### Name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary
def NBAccuracy(features_train, labels_train, features_test, labels_test):
    """ compute the accuracy of your Naive Bayes classifier """
    ### import the sklearn module for AdaBoost
    from sklearn.ensemble import AdaBoostClassifier
    ### import the sklearn module for decision tree
    from sklearn.tree import DecisionTreeClassifier

    ### create classifier tune it with n_estimators=600, learning_rate=1, DecisionTreeClassifier(max_depth=2),
    clf = AdaBoostClassifier(n_estimators=100,learning_rate=1)

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

try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass


## No Tuning
#Training time: 0.167 s
#Prediction time: 0.007 s
#0.924

## n_estimators=100,learning_rate=1
#Training time: 0.294 s
#Prediction time: 0.013 s
#0.924