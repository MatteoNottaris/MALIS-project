
import numpy as np 
import pandas as pd

from sklearn.neural_network import MLPRegressor 
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import StandardScaler

from sklearn import model_selection as ms

from sklearn.impute import SimpleImputer

my_file = 'C:/Users/matno/Desktop/Télecom/2A/MALIS/Project/GIT/MALIS-project/Code_python/Data/training/training_setV2.xlsx'


def neuralNetwork_param(file):
    dataSet = pd.read_excel(file)
    dataSet = dataSet.drop([0],axis=0)
    dataSet = dataSet.drop(columns=0, axis=1)
    
    X = dataSet.drop(columns=[1,2])
    y = dataSet[[1]]
    print(y[1])
    y['exp'] = np.exp(y[1].astype(int))
    y = y[['exp']]
    print(y)
    
    
    
    X_train,X_test,y_train,y_test=ms.train_test_split( X, y, test_size=0.20, random_state=0)
    

    regr = MLPRegressor(max_iter = 5000).fit(X_train,y_train)
    
    layers = [(19,2),(19,20,2),(19,30,2),(19,40,2),(19,50,2),(19,10,10,2),(19,20,20,2),(19,30,30,2),(19,40,40,2),(19,50,50,19)]                

    check_parameters = {
    'hidden_layer_sizes': layers,
    'activation': ['logistic'],
    'solver': ['sgd', 'adam'],
    'alpha': [0.0001, 0.5],
    'learning_rate': ['constant','adaptive'],
    }

    gridsearchcv = GridSearchCV(regr, check_parameters,n_jobs=-1,cv=5)
    gridsearchcv.fit(X_test, y_test)
    print('Best parameters found:\n', gridsearchcv.best_params_)

#print(neuralNetwork_param(my_file))

def neuralNetwork_error(lrate,solv,layer,func,rate,iters,file):
    dataSet = pd.read_excel(file)
    dataSet = dataSet.drop([0],axis=0)
    dataSet = dataSet.drop(columns=0, axis=1)
    
    X = dataSet.drop(columns=[1,2])
    y = dataSet[[1]]
    y['2'] = 1000*(y[1].astype(int))
    y = y[['2']]
    print(y)
    X_train,X_test,y_train,y_test=ms.train_test_split( X, y, test_size=0.20, random_state=0)

    regr = MLPRegressor(solver=solv,learning_rate=lrate,activation=func,hidden_layer_sizes=layer,alpha=rate,max_iter = iters,random_state=1).fit(X_train,y_train)
    
    output = (regr.predict(X_test))/1000
    y_test =(y_test)/1000
    y_train = y_train/1000
    
    
    print(output)
    print(y_test)
    
    return(mean_squared_error(output, y_test),mean_squared_error(regr.predict(X_train)/1000,y_train))

#print(neuralNetwork_error('constant','sgd',1000,'tanh', 0.1, 10000, my_file))
#print(neuralNetwork_error('constant','sgd',100,'logistic', 0.1, 10000, my_file))
#print(neuralNetwork_error('constant','adam',100,'relu', 0.1, 10000, my_file))
#print(neuralNetwork_error('adaptive','adam',10,'identity', 0.001, 10000, my_file))
