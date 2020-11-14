#This file is extracting data from AlphaVantage

#The following functions will be used in RSI-FirstPart.py



#My APIKEY for Alphavantage
my_APIKEY = '9AZS79EDFOZ47YKP'



#Importation of packages
from alpha_vantage.foreignexchange import ForeignExchange
from alpha_vantage.techindicators import TechIndicators








#This function returns the data from the RSI indicator
def getRSI (APIKEY, interv, sj, moment, timePeriod, MyPath):
    AlphVantage = TechIndicators(key = APIKEY, output_format = 'pandas')
    data, meta_data = AlphVantage.get_rsi(symbol=sj, interval=interv, time_period=timePeriod, series_type = moment)
    #extracting the datetimeIndex, converting it to np.array and then adding it to data
    new_array = data.index.strftime('%Y-%m-%d %H:%M:%S')
    data['date'] = new_array
    #converting data to excel, more readable
    data.to_excel(MyPath + 'RSI_updated.xlsx', index = False)
    return data







#This function returns the data from the dual currency cur1/cur2 every WEEK
def getDualCurrency (APIKEY, cur1, cur2, MyPath):
    AlphaVantage = ForeignExchange(key=APIKEY,output_format='pandas')
    data, meta_data = AlphaVantage.get_currency_exchange_weekly(from_symbol=cur1,to_symbol=cur2)
    #extracting the datetimeIndex, converting it to np.array and then adding it to data
    new_array = data.index.strftime('%Y-%m-%d %H:%M:%S')
    data['date'] = new_array
    #converting data to excel, more readable
    data.to_excel(MyPath + 'EURUSD_updated.xlsx', index = False)
    return (data)


