# This script is supposed to create a set of data in order to train a neural network






############################################################################################################################


#                   I) First we need to extract the RSI data from Alphavantage 

#Importation of packages
import os 
os.chdir('C:/Users/matno/Desktop/Télecom/2A/MALIS/Project/GIT/MALIS-project/Code_python')
import Extraction


#My APIKEY for Alphavantage
my_APIKEY = '9AZS79EDFOZ47YKP'

#Useful variables
my_interval = 'weekly'
my_sj = 'EURUSD'
my_moment = 'high'
my_time_period = 14
currency1 = 'EUR'
currency2 = 'USD'
my_Path = 'C:/Users/matno/Desktop/Télecom/2A/MALIS/Project/GIT/MALIS-project/Code_python/Data/'




#This function is extracting all the data from AlphaVantage and updating the corresponding files on the computer
def updateFiles ():
    
    #updating the RSIfile
    Extraction.getRSI(my_APIKEY, my_interval, my_sj, my_moment, my_time_period, my_Path)
    
    #updating the EURUSDfile
    Extraction.getDualCurrency(my_APIKEY, currency1, currency2, my_Path)
    
    return()

############################################################################################################################



#                    II) Secondly we need to develop the algorithms to generate the set


#Importation of packages
import numpy as np
import pandas as pd



#Useful variables
parameter1 = 70
parameter2 = 30

InitAmount =  1000000




#This function is the main function generating the set of data for training the neural network
def main ():
    
    #first extract data and update the corresponding files
    updateFiles()
    
    #getting all data files name in a list
    DataType = getDataType(my_Path)
    #create a panda dictionnary with all data
    data = []
    for i in range(len(DataType)):
        DataArray = dataExcel(DataType[0][i])
        data.append(DataArray)
    DataDic = pd.Series(data)
    DataDic.index = DataType[1]
    
    
    
    
    




#This function is calculating the performance 
        #amount1 is the actual amount we have at the end of the week when we listened to the RSI 
        #amount2 is the amount we would have if we wasn't listening to RSI
def perf(amount1, amount2):
    perf = (amount1 - amount2)/amount1
    return(perf * 100)




#This function is returning a RSI signal
        #inputs : parameter1 and parameter2 (deciding whether it is OS or OB)
                #:RSIval is the actual RSI value
        #outputs : if we have 1 in return it means it is oversold
            #: if we have 2 in return it means the sj is overbought
            #: if we have -1 in return it means the RSI cannot give any advice
def RSIsignal(RSIval):
    if RSIval >= parameter2:
        return (2)
    elif RSIval<= parameter1:
        return(1)
    else:
        return(-1)
    
    
 
    
#This function is extracting the data from the excel files and return a list with the content of the excel sheets
def dataExcel (FileName):
    data = pd.read_excel (my_Path + FileName)
    return(data)




#This function is returning a list of all data type in my_Path
def getDataType(path):
    FilesNames = []
    FilesNickNames = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            if '.xlsx' in file:
                FilesNames.append(file)
                FilesNickNames.append(file.replace('_updated.xlsx','',1))
    return(FilesNames, FilesNickNames)
