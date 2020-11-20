#This file is extracting data from AlphaVantage

#The following functions will be used in RSI-FirstPart.py



#Importation of packages
from alpha_vantage.foreignexchange import ForeignExchange
from alpha_vantage.techindicators import TechIndicators
from alpha_vantage.timeseries import TimeSeries

import yfinance as yf
import datetime 






#This function returns the data from the RSI indicator
def getRSI (APIKEY, Path):
    AlphVantage = TechIndicators(key = APIKEY, output_format = 'pandas')
    data, meta_data = AlphVantage.get_rsi(symbol='EURUSD', interval='daily', time_period=14, series_type = 'high')
    #extracting the datetimeIndex, converting it to np.array and then adding it to data
    new_array = data.index.strftime('%Y-%m-%d')
    data.insert(0, 'date', new_array)
    #converting data to excel, more readable
    data.to_excel(Path + 'RSI.xlsx', index = False)
    return data


#This function returns the data from the dual currency cur1/cur2 every WEEK
def getDualCurrency (APIKEY, Path):
    AlphaVantage = ForeignExchange(key=APIKEY,output_format='pandas')
    data, meta_data = AlphaVantage.get_currency_exchange_daily(from_symbol='EUR',to_symbol='USD')
    #extracting the datetimeIndex, converting it to np.array and then adding it to data
    new_array = data.index.strftime('%Y-%m-%d')
    data.insert(0, 'date', new_array)
    data = data[::-1]
    #converting data to excel, more readable
    data.to_excel(Path + 'EURUSD.xlsx', index = False)
    return (data)


#This function returns the data from the NASDAQ every day
def getNASDAQ (Path):
    todayDate = datetime.date.today().strftime("%Y-%m-%d")
    data = yf.download("^IXIC", start= "2000-01-01", end = todayDate, interval = "1d")
    #extracting the datetimeIndex, converting it to np.array and then adding it to data
    new_array = data.index.strftime('%Y-%m-%d')
    data.insert(0, 'date', new_array)
    #converting data to excel, more readable
    data.to_excel(Path + 'NASDAQ.xlsx', index = False)
    return (data)


#This function returns the data from the DOwJones every day
def getDOWJONES (Path):
    todayDate = datetime.date.today().strftime("%Y-%m-%d")
    data = yf.download("^DJI", start= "2000-01-01", end = todayDate, interval = "1d")
    #extracting the datetimeIndex, converting it to np.array and then adding it to data
    new_array = data.index.strftime('%Y-%m-%d')
    data.insert(0, 'date', new_array)
    #converting data to excel, more readable
    data.to_excel(Path + 'DOWJONES.xlsx', index = False)
    return (data)


#This function returns the data from the SP500 every day
def getSP500(Path):
    todayDate = datetime.date.today().strftime("%Y-%m-%d")
    data = yf.download("^GSPC", start= "2000-01-01", end = todayDate, interval = "1d")
    #extracting the datetimeIndex, converting it to np.array and then adding it to data
    new_array = data.index.strftime('%Y-%m-%d')
    data.insert(0, 'date', new_array)
    #converting data to excel, more readable
    data.to_excel(Path + 'SP500.xlsx', index = False)
    return (data)

#This function returns the data from the FTSE100 every day
def getFTSE100(Path):
    todayDate = datetime.date.today().strftime("%Y-%m-%d")
    data = yf.download("^FTSE", start= "2000-01-01", end = todayDate, interval = "1d")
    #extracting the datetimeIndex, converting it to np.array and then adding it to data
    new_array = data.index.strftime('%Y-%m-%d')
    data.insert(0, 'date', new_array)
    #converting data to excel, more readable
    data.to_excel(Path + 'FTSE100.xlsx', index = False)
    return (data)

#This function returns the data from the DAX every day
def getDAX(Path):
    todayDate = datetime.date.today().strftime("%Y-%m-%d")
    data = yf.download("^GDAXI", start= "2000-01-01", end = todayDate, interval = "1d")
    #extracting the datetimeIndex, converting it to np.array and then adding it to data
    new_array = data.index.strftime('%Y-%m-%d')
    data.insert(0, 'date', new_array)
    #converting data to excel, more readable
    data.to_excel(Path + 'DAX.xlsx', index = False)
    return (data)


#This function returns the data from the EUROSTOXX600 every day
def getSTOXX600(Path):
    todayDate = datetime.date.today().strftime("%Y-%m-%d")
    data = yf.download("^STOXX", start= "2000-01-01", end = todayDate, interval = "1d")
    #extracting the datetimeIndex, converting it to np.array and then adding it to data
    new_array = data.index.strftime('%Y-%m-%d')
    data.insert(0, 'date', new_array)
    #converting data to excel, more readable
    data.to_excel(Path + 'STOXX600.xlsx', index = False)
    return (data)


#This function returns the data from the EUROSTOXX50 every day
def getSTOXX50E(Path):
    todayDate = datetime.date.today().strftime("%Y-%m-%d")
    data = yf.download("^STOXX50E", start= "2000-01-01", end = todayDate, interval = "1d")
    #extracting the datetimeIndex, converting it to np.array and then adding it to data
    new_array = data.index.strftime('%Y-%m-%d')
    data.insert(0, 'date', new_array)
    #converting data to excel, more readable
    data.to_excel(Path + 'STOXX50E.xlsx', index = False)
    return (data)


#This function returns the data from the HSCEI every day
def getHSCEI(Path):
    todayDate = datetime.date.today().strftime("%Y-%m-%d")
    data = yf.download("^HSCE", start= "2000-01-01", end = todayDate, interval = "1d")
    #extracting the datetimeIndex, converting it to np.array and then adding it to data
    new_array = data.index.strftime('%Y-%m-%d')
    data.insert(0, 'date', new_array)
    #converting data to excel, more readable
    data.to_excel(Path + 'HSCEI.xlsx', index = False)
    return (data)


#This function returns the data from the HSCEI every day
def getNIKKEI(Path):
    todayDate = datetime.date.today().strftime("%Y-%m-%d")
    data = yf.download("^N225", start= "2000-01-01", end = todayDate, interval = "1d")
    #extracting the datetimeIndex, converting it to np.array and then adding it to data
    new_array = data.index.strftime('%Y-%m-%d')
    data.insert(0, 'date', new_array)
    #converting data to excel, more readable
    data.to_excel(Path + 'NIKKEI.xlsx', index = False)
    return (data)


#This function returns the data from the HSCEI every day
def getCAC40(Path):
    todayDate = datetime.date.today().strftime("%Y-%m-%d")
    data = yf.download("^FCHI", start= "2000-01-01", end = todayDate, interval = "1d")
    #extracting the datetimeIndex, converting it to np.array and then adding it to data
    new_array = data.index.strftime('%Y-%m-%d')
    data.insert(0, 'date', new_array)
    #converting data to excel, more readable
    data.to_excel(Path + 'CAC40.xlsx', index = False)
    return (data)