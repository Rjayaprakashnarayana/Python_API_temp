import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score 
import pickle
data = pd.read_csv('Training.csv')
X = data.iloc[:,:-1]
#print(X.columns)
Y = data.iloc[:,-1]
#print(Y)
X= X.values
#print(X)
Y = Y.values
#print(Y)
classifier = DecisionTreeClassifier()
classifier.fit(X,Y)
test_data= pd.read_csv('Testing.csv')
X_test = test_data.iloc[:,:-1].values
Y_test= test_data.iloc[:,-1].values
Y_pred=classifier.predict(X_test)
#print(accuracy_score(Y_pred,Y_test))
f = open('model.pkl','wb')
pickle.dump(classifier,f)
f.close()