# Data Preprocessing Template

# Importing the libraries
# a library is a tool which is used to do a specific job: you give it an input and it gives you an output
#for maths
import numpy as np
#for maths
import matplotlib.pyplot as plt
#import and manage dataset
import pandas as pd

# Importing the dataset
#indep variables =Country,Age and Salary; Dep variable=purchased
dataset = pd.read_csv('Data.csv')
#we will produce a matrix and put the indep variables (country, age, salary) inside
X = dataset.iloc[:, :-1].values #[all the lines, all the column except the last one]
y = dataset.iloc[:, 3].values#[all the lines, thrid column]


# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)


# Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train)"""