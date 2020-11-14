# This script is supposed to create a set of data in order to train a neural network




#My APIKEY for Alphavantage
my_APIKEY = '9AZS79EDFOZ47YKP'




#                   I) First we need to extract the RSI data from Alphavantage 

#Importation of packages
import Extraction



#Useful variables
my_interval = 'weekly'
my_sj = 'EURUSD'
my_moment = 'high'
my_time_period = 14
currency1 = 'EUR'
currency2 = 'USD'
my_Path = 'C:/Users/matno/Desktop/Télecom/2A/MALIS/Project/GIT/MALIS-project/Code_python/Data/'




#RSIfile is the csv file with the updated value of RSI for EURUSD (weekly)
RSIfile = Extraction.getRSI(my_APIKEY, my_interval, my_sj, my_moment, my_time_period, my_Path)

#EURUSDfile is the csv file with the updated value of EURUSD (weekly)
RSIfile = Extraction.getDualCurrency(my_APIKEY, currency1, currency2, my_Path)







    
