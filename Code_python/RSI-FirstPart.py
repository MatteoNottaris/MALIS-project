# This script is supposed to create a set of data in order to train a neural network






############################################################################################################################


#                   I) First we need to extract the RSI data from Alphavantage 

#Importation of packages
import os 
os.chdir('C:/Users/matno/Desktop/Télecom/2A/MALIS/Project/GIT/MALIS-project/Code_python')
import Extraction
import numpy as np
import pandas as pd


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

parameter1 = 70
parameter2 = 30
InitAmount =  1000000



#This function is extracting all the data from AlphaVantage and updating the corresponding files on the computer
def updateFiles ():
    
    #updating the RSIfile
    Extraction.getRSI(my_APIKEY, my_interval, my_sj, my_moment, my_time_period, my_Path)
    
    #updating the EURUSDfile
    Extraction.getDualCurrency(my_APIKEY, currency1, currency2, my_Path)
    
    return()

############################################################################################################################



#                    II) Secondly we need to develop the algorithms to generate the set




#This function is the main function generating the set of data for training the neural network
def main ():
    
    #first extract data and update the corresponding files
    #updateFiles()
    

    #creating a panda dictionnary with all data
    DataDico = formatData()
    
    #updating the DataDico concidering all data set size
    new_DataDico = updateData(DataDico)

    return()



###########################################################################################################################




#                                III) We need to develop tools functions in order to create main




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
    
    
 
    
#This function formatData() is extracting the data from the excel files and return a dictionnary with the content of the excel sheets
#dataExcel() allows to read an excel File
#getFiles () allows to get all excel files in a file
def formatData():
    data = []
    FilesNames = getFiles(my_Path)
    for i in range(len(FilesNames)):
        DataArray = dataExcel(FilesNames[i] + '.xlsx')
        date = DataArray.loc[:,'date']
        value = DataArray.iloc[:,[1]].values.tolist()
        TemporaryDic = pd.Series(value)
        TemporaryDic.index = date
        data.append(TemporaryDic)
    DataDic = pd.Series(data)
    DataDic.index = FilesNames
    return(DataDic)
    
def dataExcel (FileName):
    data = pd.read_excel (my_Path + FileName)
    return(data)


def getFiles(path):
    FilesNames = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            if '.xlsx' in file:
                FilesNames.append(file.replace('.xlsx','',1))
    return(FilesNames)



#####                  NOT WORKING


#This function is extracting from all the data set the intersection set usable
# set1 and set2 are supposed to be pd.Series
def updateData(Dico):
    
    #first we need to find the min and the max Date to all the data set
    commonDate = []
    for item1 in Dico.iteritems:
        for item2 in Dico.iteritems:
            result = intersectionSet(item1[1], item2[1])
            if result[0] > commonDate[0]:
                commonDate[0] = result[0]
            if result[1] < commonDate[1]:
                commonDate [1] = result[1]
    
    #secondly we have to update every data set accordingly
    for item1 in Dico.iteritems:
        for item2 in item1[0].iteritems:
            if item2[0] < commonDate[0] or item2[0] > commonDate[1]:
                item1[0].drop(item2[0])
                
    return(Dico)   
        
def intersectionSet (set1, set2):
    min1 = min(set1.index)
    min2 = min(set2.index)
    EarliestDate = max([min1,min2])
    max1 = max(set1.index)
    max2 = max(set2.index)
    LatestDate = min([max1,max2])
    
    return(EarliestDate, LatestDate)

print(main())