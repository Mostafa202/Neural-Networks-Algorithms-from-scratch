# Data Preprocessing Template

# Importing the libraries
import pandas as pd
import matplotlib.pyplot as plt
import hebb as hb
import perceptron as per
import form as fm

# Importing the dataset

def set_dataset(pass_data):
    dataset = pd.read_csv(pass_data)
    return dataset
    




"""
x = dataset.iloc[:,:-1].values
y = dataset.iloc[:,7:8].values
from sklearn.preprocessing import *

s=StandardScaler()
x=s.fit_transform(x)

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)

y_hat_hebbian=hb.hebb(1,1,[0,0,0,0,0,0,0])(x_train,y_train,x_test,y_test)
y_hat_perceptron=per.perceptron(1,1,[0,0,0,0,0,0,0])(x_train,y_train,x_test,y_test)
"""
