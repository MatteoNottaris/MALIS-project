
import numpy as np #linear algebra
import pandas as pd #datapreprocessing, CSV file I/O
import seaborn as sns #for plotting graphs
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt

from sklearn.neural_network import MLPRegressor

my_file = 'C:/Users/matno/Desktop/Télecom/2A/MALIS/Project/GIT/MALIS-project/Code_python/Data/training/training_set.xlsx'

def gettingSets(file):
    
    dataSet = pd.read_excel(file)
    dataSet = dataSet.to_numpy()
    dataSet = dataSet[:,1:]
    dataSet = dataSet[1:,:]
    
    dataSet=np.random.permutation(dataSet)
    n = int(np.floor(0.9 * len(dataSet)))
    X_train = dataSet[:n,2:]
    X_test = dataSet[n:,2:]
    Y_train = dataSet[:n,:1]
    Y_test = dataSet[n:,:1]

    
    return(X_train, Y_train, X_test, Y_test)

def neuralNetwork():
    dataSet = pd.read_excel(my_file)
    dataSet = dataSet.to_numpy()
    dataSet = dataSet[:,1:]
    dataSet = dataSet[1:,:]
    
    X = dataSet[2:,:]
    Y = dataSet[:2,:]
    
    X_train, X_test, Y_train, Y_test = train_test_split (X, Y, test_size = 0.30, random_state=21)
    
    regr = MLPRegressor(hidden_layer_sizes= 3, max_iter= 6000, learning_rate_init=0.1,activation='identity',random_state = 1).fit(X_train,Y_train)
    print(regr.predict(X_test))
    print(regr.score(X_test, Y_test))
    kfold = KFold(n_splits=15, random_state=21)
    cv_results = cross_val_score(regr, X_train, Y_train, cv=kfold, scoring='r2')
    plt.plot(cv_results)
    plt.show
    return()
    
print(neuralNetwork())





