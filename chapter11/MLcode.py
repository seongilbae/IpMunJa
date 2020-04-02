import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier as KNN

mr = pd.read_csv("result.csv", header=None)
 
naminglabel = [] # malware or benign
data = []

for row_index, row in mr.iterrows():
    naminglabel.append(row.ix[0]) # column 1 is m or b
    row_data = []
    for v in row.ix[1:]:
        row_data.append(ord(chr(v)))
    data.append(row_data)

# Separate test(25%) train(75%)
# d_ = data_, l_ = label_
d_train, d_test, l_train, l_test = train_test_split(data, naminglabel)
    
def trainingdata() : 
    # RF Training Data 
    clf = RandomForestClassifier() # Create RandomForest Object
    clf.fit(d_train, l_train) # Object training

    # SVM Training Data
    svm = SVC()
    svm.fit(d_train, l_train)

    #KNN Training Data
    knn = KNN(n_neighbors=2)
    knn.fit(d_train, l_train)

def predictdata() : 
   # RF Predict
    p_rf = clf.predict(d_test) # test data predict

    #SVM Predict
    p_svm = svm.predict(d_test)

    #KNN Predict
    p_knn = knn.predict(d_test)

def result() : 
    # Result RF
    RF_ac = metrics.accuracy_score(l_test, p_rf)
    RF_report = metrics.classification_report(l_test, p_rf)
    # Result SVM
    SVM_ac = metrics.accuracy_score(l_test, p_svm)
    SVM_report=metrics.classification_report(l_test, p_svm)
    # Result KNN
    KNN_ac = metrics.accuracy_score(l_test, p_knn)
    KNN_report=metrics.classification_report(l_test, p_knn)

    print("Random Forest Accuracy = %.3f" % RF_ac)
    print(RF_report+'\n')
    print("SVM Accuracy = %.3f" % SVM_ac)
    print(SVM_report+'\n')
    print("KNN Accuracy = %.3f" % KNN_ac)
    print(KNN_report)

if __name__ == "__main__" : 
    trainingdata()
    predictdata()
    result()