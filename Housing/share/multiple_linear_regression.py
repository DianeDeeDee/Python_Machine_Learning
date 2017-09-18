# Multiple Linear Regression

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from sklearn import model_selection
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.svm import SVR
from sklearn import datasets, svm


from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn import  svm
from sklearn import linear_model

# Importing the dataset
dataset = pd.read_csv('housing.csv')
dataset.columns = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']
N = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'AGE', 'DIS', 'RAD', 'TAX', 'B']
dataset.drop(N, axis=1, inplace=True)
print("----------------",list(dataset))
X = dataset.drop('MEDV', axis = 1)#dataset.iloc[:, 0:8].values
y = dataset['MEDV']

# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)


# Fitting Multiple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
mod = regressor.fit(X_train, y_train)

# Predicting the Test set results
y_pred = regressor.predict(X_test)

print("The model accuracy score=R2= ",mod.score(X_test, y_test))
print("")
print("bi coeff values= ",mod.coef_)
print("")
print("b0 value = ", (mod.intercept_))

# Visualising the Regression results
plt.scatter(y_test,y_pred)
plt.xlabel("True Values")
plt.ylabel("Predictions")
plt.savefig("True_verus_Predicted_Values.pdf")



### Stage 6: "Check the performance of the Prediction"
from sklearn.model_selection import cross_val_score
scores = cross_val_score(regressor, X_test,  regressor.predict(X_test), cv=10)
print("scores = " + str(scores))

# Compare Algorithms
# prepare configuration for cross validation test harness
seed = 5
print("1")
# prepare models
models = []
print("2")
models.append(('LR', LinearRegression()))
models.append(('svr', svm.SVR(kernel='linear')))
models.append(('random_forest', RandomForestRegressor()))
models.append(('elastic_net', linear_model.ElasticNet()))
#models.append(('LR', LogisticRegression()))
#models.append(('KNN', KNeighborsClassifier()))
#models.append(('CART', DecisionTreeClassifier()))
#models.append(('NB', GaussianNB()))
#models.append(('SVM', SVC()))
#models.append(('SVM', SVR()))

# evaluate each model in turn
results = []
names = []
#scoring = 'accuracy'
scoring = 'neg_mean_squared_error'
for name, model in models:
	kfold = model_selection.KFold(n_splits=10, random_state=seed)
	cv_results = model_selection.cross_val_score(model, X, y, cv=kfold,scoring=scoring)
	results.append(cv_results)
	print("cv_results= ",cv_results)
	names.append(name)
	msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
	print("msg= ",msg)

# boxplot algorithm comparison
fig = plt.figure()
fig.suptitle('Algorithm Comparison')
ax = fig.add_subplot(111)
plt.boxplot(results)
ax.set_xticklabels(names)
plt.savefig("AlgorithmComparison.pdf")
#plt.show()

