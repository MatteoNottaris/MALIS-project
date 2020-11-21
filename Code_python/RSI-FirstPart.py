# This script is supposed to create a set of data in order to train a neural network






############################################################################################################################


#                   I) Declaration of the importations, variables and main function 

#Importation of packages
import os 
os.chdir('C:/Users/matno/Desktop/Télecom/2A/MALIS/Project/GIT/MALIS-project/Code_python')
import Extraction
import numpy as np
import pandas as pd
import datetime 


#My APIKEY for Alphavantage
my_APIKEY = '9AZS79EDFOZ47YKP'

#Useful variables
my_Path = 'C:/Users/matno/Desktop/Télecom/2A/MALIS/Project/GIT/MALIS-project/Code_python/Data/'






#This function is the main function generating the set of data for training the neural network
def main ():
    
    #first extract data and update the corresponding files
    #updateFiles()
    

    #creating a panda dictionnary with all data
    DataDico = formatData()

    return()





############################################################################################################################

#                       II) We first need to extractthe data from AlphaVantage


#This function is extracting all the data from AlphaVantage and updating the corresponding files on the computer
def updateFiles ():
    
    #updating the RSI file
    Extraction.getRSI(my_APIKEY, my_Path)
    
    #updating the EURUSD file
    Extraction.getEURUSD(my_Path)
    
    #updating the NASDAQ file
    Extraction.getNASDAQ(my_Path)
    
    #updating the DOWJONES file
    Extraction.getDOWJONES(my_Path)
    
    #updating the SP500 file
    Extraction.getSP500(my_Path)
    
    #updating the FSTE100 file
    Extraction.getFTSE100(my_Path)
    
    #updating the DAX file
    Extraction.getDAX(my_Path)
    
    #updating the STOXX600 file
    Extraction.getSTOXX600(my_Path)
    
    #updating the STOXX50E file
    Extraction.getSTOXX50E(my_Path)
    
    #updating the HSCEI file
    Extraction.getHSCEI(my_Path)
    
    #updating the NIKKEI file
    Extraction.getNIKKEI(my_Path)
    
    #updating the CAC40 file
    Extraction.getCAC40(my_Path)
    
    #updating the XAUUSD file
    Extraction.getGOLD(my_Path)
    
    #updating the OIL file
    Extraction.getOIL(my_Path)
    
    #updating the USDJPY file
    Extraction.getUSDJPY(my_Path)
    
    #updating the USDCNY file
    Extraction.getUSDCNY(my_Path)
    
    #updating the VIX file
    Extraction.getVIX(my_Path)
    
    #updating the DOLLAR INDEX file
    Extraction.getDOLLARINDEX(my_Path)
    
    #updating the TAUX US 10 file
    Extraction.getTAUX10US(my_Path)
    
    #updating the TAUX US 5 file
    Extraction.getTAUX5US(my_Path)
    
    
    return()


###########################################################################################################################




#                                III) We need to adjust the data to be easily used

    
    
#This function formatData() is extracting the data from the excel files and return a dictionnary with the content of the excel sheets
#dataExcel() allows to read an excel File
#getFiles () allows to get all excel files in a file
#intersectionDate (set1, set2) allows to compare two data set and return the common dates
#
def formatData():
    #we initialize commonDate[] with date of day
    todayDate = datetime.date.today().strftime("%Y-%m-%d")
    commonDate = ["1900-01-01", todayDate]
    data = []
    DicoList = []
    FilesNames = getFiles(my_Path)
    for i in range(len(FilesNames)):
        DataArray = dataExcel(FilesNames[i] + '.xlsx')
        DataArray = DataArray.to_numpy()
        data.append(DataArray)
    #commonDate is a two element list corresponding to the earliest and latest date common to all sets
    for i in range(len(data) - 1):
        result = intersectionDate(data[i],data[i+1])
        if result[0] > commonDate[0]:
            commonDate[0] = result[0]
        if result[1] < commonDate[1]:
            commonDate[1] = result[1]
    #updating every set with the common dates
    for i in range(len(data)):
        data[i] = updateData(data[i], commonDate[0], commonDate[1])
    #transforming every array in pd.Series
    for i in range (len(data)):
        date = data[i][:,0]
        value = data[i][:,1]
        TemporaryDic = pd.Series(value)
        TemporaryDic.index = date
        DicoList.append(TemporaryDic)
    #removing some dates inside commonDate using removeSomeDate()
    for i in range(len(DicoList)-1):
        result = removeSomeDate(DicoList[i],DicoList[i+1])
        DicoList[i] = result[0]
        DicoList[i+1] = result[1]
    for i in range(len(DicoList)-1,0, -1):
        result = removeSomeDate(DicoList[i],DicoList[i-1])
        DicoList[i] = result[0]
        DicoList[i-1] = result[1]
    #creating a main Dictionary containing dictionnary for every set
    DataDic = pd.Series(DicoList)
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
    

#This function is slicing data array in order to match the intersection date
def updateData(set, earlydate, latedate):
    i = 0
    while set[i][0] != earlydate:
        i+=1
    temp_set = set[i:]
    i = 1
    while temp_set[len(temp_set)-i][0] != latedate:
        i+=1
    set = temp_set [:len(temp_set)-i+1]
    
    return (set)

#This function is determining between to data set the earliest and latest common dates 
def intersectionDate (set1, set2):
    min1 = np.amin(set1, axis = 0)[0]
    min2 = np.amin(set2, axis = 0)[0]
    EarliestDate = max([min1,min2])
    max1 = np.amax(set1, axis = 0)[0]
    max2 = np.amax(set1, axis = 0)[0]
    LatestDate = min([max1,max2])
    
    return(EarliestDate, LatestDate)


#This function is removing the date present in Dico1 and not in Dico2 and vice versa
def removeSomeDate (Dico1,Dico2):
    for index in Dico1.items():
        if not Dico2.get(index[0]):
            Dico1 = Dico1.drop(labels = index[0])
    for index in Dico2.items():
        if not Dico1.get(index[0]):
            Dico2 = Dico2.drop(index[0])
    return (Dico1, Dico2)

##########################################################################################################################


#                                   IV) Tools




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
def RSIsignal(RSIval, parameter1, parameter2):
    if RSIval >= parameter2:
        return (2)
    elif RSIval<= parameter1:
        return(1)
    else:
        return(-1)
    
        




print(main())