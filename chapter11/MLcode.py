import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier as KNN

csvfile = pd.read_csv("result.csv", header=None)
 
naminglabel = []
data = []

for row_index, row in csvfile.iterrows():
    naminglabel.append(row.ix[0])
    tmp = []
    for v in row.ix[1:]:
        tmp.append(ord(chr(v)))
    data.append(tmp)

d_train, d_test, l_train, l_test = train_test_split(data, naminglabel)

def trainingdata() : 
    rftrain = RandomForestClassifier() 
    rftrain.fit(d_train, l_train)

    svmtrain = SVC()
    svmtrain.fit(d_train, l_train)

    knntrain = KNN(n_neighbors=2)
    knntrain.fit(d_train, l_train)
    
    return rftrain, svmtrain, knntrain

def predictdata(a, b, c) : 
    rfpredict = a.predict(d_test)
    svmpredict = b.predict(d_test)
    knnpredict = c.predict(d_test)
    
    return rfpredict, svmpredict, knnpredict

def result(x, y, z) : 
    rfacc = metrics.accuracy_score(l_test, x)
    rffinal = metrics.classification_report(l_test, x)
    svmacc = metrics.accuracy_score(l_test, y)
    svmfinal=metrics.classification_report(l_test, y)
    knnacc = metrics.accuracy_score(l_test, z)
    knnfinal=metrics.classification_report(l_test, z)

    print("Random Forest Accuracy = %.3f" % rfacc)
    print(rffinal+'\n')
    print("SVM Accuracy = %.3f" % svmacc)
    print(svmfinal+'\n')
    print("KNN Accuracy = %.3f" % knnacc)
    print(knnfinal)
    
a, b, c = trainingdata()
x, y, z = predictdata(a, b, c)
result(x, y, z)