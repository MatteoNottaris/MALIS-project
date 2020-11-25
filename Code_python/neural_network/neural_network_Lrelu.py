# This file is a neural network which will be used for our project


##########################################################################################################################

#                                                    I) Importations



from NeuralNetwork_class import MLP
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

my_file = 'C:/Users/matno/Desktop/Télecom/2A/MALIS/Project/GIT/MALIS-project/Code_python/Data/training/training_set.xlsx'




###########################################################################################################################


#                                                   II) Functions

alpha = 0.1

def Lrelu(a):
    res = np.where(a >0, a, alpha * a)
    return(res)


def d_Lrelu(a):
    res = np.where(a >0, 1, alpha)
    return(res)



def d_sigmoid(a) :
    '''
    Derivative of sigmoid activation function. It can work with single inputs or vectors or matrices.
    Return the sigmoid derivative of a
    '''

    
    sigmoid = MLP.sigmoid(a) 
    
    der_sig = sigmoid * (1 - sigmoid)
    
    return (der_sig)

    
MLP.d_sigmoid=d_sigmoid



# **3. Feedforward function**
# 
# Write a function which performs the forward operation from input to output layer. Remember you have len(self.layers) number of layers and each layer has its own parameters:
# 1. self.layer[0].W are the weights between input and 1st hidden layer
# 2. self.layer[0].b are the biases of the 1st hidden layer
# 3. ...
# 
# Each layer has as activation function the sigmoid function



def forward(self, x) :
    '''
    Forward function. From input layer to output layer. Input can handle 1D or 2D inputs.

    INPUTS:
    - x : numpy array of size NxD, where N is the number of samples, D is the number of input dimensions referred as n_input before

    OUTPUTS:
    - y_hat : numpy array of size NxC, where C is the number of classes
    '''
    
    self.layer[0].a = np.array(x @ self.layer[0].W.T + self.layer[0].b, dtype = np.float64 )
    self.layer[0].z = MLP.sigmoid(self.layer[0].a)
    for j in range (1,len(self.layer)):
        if j != len(self.layer)-1:
            self.layer[j].a = np.array(self.layer[j - 1].z @ self.layer[j].W.T + self.layer[j].b, dtype = np.float64)
            self.layer[j].z = MLP.sigmoid(self.layer[j].a)
        else:
            self.layer[j].a = np.array(self.layer[j - 1].z @ self.layer[j].W.T + self.layer[j].b, dtype = np.float64)
            self.layer[j].z = Lrelu(self.layer[j].a)
            
    y_hat = self.layer[len(self.layer) - 1].z
        

    return y_hat

MLP.forward=forward



# **4. Loss function**



def loss(y_hat, y) :
    '''
    Compute the loss between y_hat and y! they can be 1D or 2D arrays!

    INPUTS:
    - y_hat : numpy array of size NxC, N number of samples, C number of classes. It contains the estimated values of y
    - y : numpy array of size NxC with one 1 in each row, corresponding to the correct class for that sample

    OUTPUTS:
    - L : MSE loss
    '''

    print(y_hat)
    print(y)

    N = np.size(y_hat,0)
    C = np.size(y_hat,1)
    L = 0
    
    sum1 = 0
    for i in range(N):
        sum2 = 0
        for j in range(C):
            sum2 += (y_hat[i][j] - y[i][j])**2
        sum1 += sum2
    
    L = 1/(2*N) * sum1


    return L

MLP.loss=loss


# **6. Backpropagation**


def backpropagation(self,x,y,y_hat,learning_rate) :
    '''
    Backpropagate the error from last layer to input layer and then update the parameters

    INPUTS:
    - y_hat : numpy array of size NxC, C number of classes. It contains the estimated values of y
    -y : numpy array of size NxC with correct values of y

    OUTPUTS: (compute the error at the different levels and for each layer)
    - d_a
    - d_z
    - delta_L
    - delta_l
    - d_W
    - d_b
    '''
# compute gradients


    
    delta_L = y_hat - y
    delta_l = []
    
    self.layer[len(self.layer) -1].d_a = np.multiply(delta_L,d_Lrelu(self.layer[len(self.layer)-1].a))
    self.layer[len(self.layer) -1].d_z = delta_L
    delta_l.insert(0,self.layer[len(self.layer) -1].d_z)
    
    for i in range (len(self.layer)-2,0, -1):
        self.layer[i].d_z = self.layer[i+1].d_a @ self.layer[i+1].W
        self.layer[i].d_a = np.multiply(self.layer[i].d_z,MLP.d_sigmoid(self.layer[i].a))
        delta_l.insert(0,self.layer[i].d_z)
    
    self.layer[0].d_z = self.layer[1].d_a @ self.layer[1].W
    self.layer[0].d_a = np.multiply(self.layer[0].d_z,MLP.d_sigmoid(self.layer[0].a))
    delta_l.insert(0,self.layer[0].d_z)


# apply gradients
    # just one for loop passing through all layers is sufficient
    # apply the gradients only to self.layer[i].b and self.layer[i].W

    
    self.layer[0].d_W = self.layer[0].d_a.T @ x
    self.layer[0].d_b = self.layer[0].d_a
    
    self.layer[0].W =self.layer[0].W - learning_rate * (self.layer[0].d_W)
    self.layer[0].b = self.layer[0].b - learning_rate * (self.layer[0].d_b)
    
    for i in range (1,len(self.layer)):
        self.layer[i].d_W = self.layer[i].d_a.T @ self.layer[i-1].z
        self.layer[i].d_b = self.layer[i].d_a
        self.layer[i].W =self.layer[i].W - learning_rate * (self.layer[i].d_W)
        self.layer[i].b =self.layer[i].b - learning_rate * (self.layer[i].d_b)
    
    return(delta_L, delta_l)

    
MLP.backpropagation=backpropagation



########################################################################################################################


#                                 III) Neural Network



def gettingSets(file):
    
    dataSet = pd.read_excel(file)
    dataSet = dataSet.to_numpy()
    dataSet = dataSet[:,1:]
    dataSet = dataSet[1:,:]
    
    dataSet=np.random.permutation(dataSet)
    n = int(np.floor(0.9 * len(dataSet)))
    X_train = dataSet[:n,2:]
    X_test = dataSet[n:,2:]
    Y_train = dataSet[:n,:2]
    Y_test = dataSet[n:,:2]

    
    return(X_train, Y_train, X_test, Y_test)


def train():
    # Neural Network (NN) parameters
    epochs=100
    learning_rate=0.6
    verbose=True
    print_every_k=10
    
    set = gettingSets(my_file)
    x_train = set[0]
    y_train = set[1]
    x_test = set[2]
    y_test = set[3]
    
    # Initialization of the NN
        #first value of the vecteur is the number of input (=19 corresponding to the number of indicator for a market photo)
        #second value is the number of neuron on the first layer
        #.....
        # last value is the number of neuron on the last layer (=2 corresponding to the RSI parameters)
    NN1 = MLP([19, 10, 2])
    print('TRAINING')
    # Training
    NN1.training(x_train,y_train,learning_rate,epochs,verbose,print_every_k)
    # Compute the training loss and accuracy after having completer the training
    y_hat=NN1.forward(x_train)
    print('final : loss = %.3e%%'%(MLP.loss(y_hat,y_train)))
    
    # Test
    print('\nTEST')
    
    y_hat=NN1.forward(x_test)
    print('loss = %.3e%%\n'%(MLP.loss(y_hat,y_test)))
    
    plt.plot(list(range(epochs)),NN1.losses,c='r',marker='o',ls='--');
    plt.title("Training Loss")
    plt.xlabel("epochs")
    plt.ylabel("loss value")
    plt.show()
    
    return() 


print(train())