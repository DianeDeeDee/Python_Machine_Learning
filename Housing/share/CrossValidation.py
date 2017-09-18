
# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math

from sklearn import datasets
from sklearn import linear_model
from sklearn.ensemble import RandomForestRegressor
from sklearn import model_selection
from sklearn import cross_validation
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import cross_val_score

# Importing the dataset
dataset = pd.read_csv('housing.csv')
print("----------------",list(dataset))
X = dataset[['CRIM', 'CHAS', 'RM', 'DIS', 'PTRATIO', 'B', 'LSTAT']]#.drop('MEDV', axis = 1)
y = dataset['MEDV']

from sklearn import linear_model
lm = linear_model.LinearRegression()
model = lm.fit(dataset.as_matrix(['RM']), dataset.as_matrix(['MEDV']))
predictions = lm.predict(dataset.as_matrix(['RM']))
#The print function would print the first 5 predictions for y
print("dataset.as_matrix(['RM'])[0:5]= " ,((dataset.as_matrix(['RM']))[0:5]))
print("(predictions)[0:5]= ",(predictions)[0:5])
print("Price predictions for a 5 room house= ",lm.predict([[5]]))
print("Price predictions for a 6 room house= ",lm.predict([[6]]))
print("Price predictions for a 7 room house= ",lm.predict([[7]]))
print("Price predictions for a 8 room house= ",lm.predict([[8]]))
print("")

validation_scores = cross_validation.cross_val_score(model,dataset.as_matrix(['RM', 'PTRATIO', 'LSTAT']),dataset.as_matrix(['MEDV']),cv=10,scoring='neg_mean_squared_error')
print("Price Accuracy for 10 CV (between 3 variables and the prices):",validation_scores)
#print("Average Error on R2= %0.2f" % math.sqrt(- np.mean(validation_scores)))
#print("Average Price Accracy: %0.2f" % ( np.mean(validation_scores)))
print("Average Price Accuracy: %0.2f (+/- %0.2f)" % (np.mean(validation_scores), math.sqrt(- np.mean(validation_scores))))
print("")
models = []
results = []
names =[]

print("Comparison between few models: linear_regression, elastic_net, random_forest, SVR:")
from sklearn import datasets, svm
models = {'linear_regression': linear_model.LinearRegression(),'elastic_net': linear_model.ElasticNet(),'random_forest': RandomForestRegressor(),'svr': svm.SVR(kernel='linear'),}#'NB':GaussianNB(),}
for name, mod in models.items():
	names.append(name)
	validation_scores2 = cross_validation.cross_val_score(mod,dataset.as_matrix(['RM', 'PTRATIO', 'LSTAT']),dataset.as_matrix(['MEDV']),cv=10,scoring='neg_mean_squared_error')
	results.append(validation_scores2)
	print("The testing model is:",name)
	print("Price Accuracy for 10 CV %0.2f= ", validation_scores2)
	print("Average Price Accuracy: %0.2f (+/- %0.2f)" % (np.mean(validation_scores2), math.sqrt(- np.mean(validation_scores2))))

# boxplot algorithm comparison
fig = plt.figure()
fig.suptitle('Average error per algorithm')
plt.xlabel("Model Names")
plt.ylabel("Error")
ax = fig.add_subplot(111)
plt.boxplot(results)
ax.set_xticklabels(names)
#plt.show()
plt.savefig("AlgorithmComparison.pdf")
