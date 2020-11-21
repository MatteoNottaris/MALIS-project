#This file is extracting data from AlphaVantage

#The following functions will be used in RSI-FirstPart.py



#Importation of packages
from alpha_vantage.foreignexchange import ForeignExchange
from alpha_vantage.techindicators import TechIndicators

import yfinance as yf
from yahoofinancials import YahooFinancials

import datetime 
import pandas as pd






#This function returns the data from the RSI indicator for EURUSD every day
def getRSI (APIKEY, Path):
    AlphVantage = TechIndicators(key = APIKEY, output_format = 'pandas')
    data, meta_data = AlphVantage.get_rsi(symbol='EURUSD', interval='daily', time_period=14, series_type = 'high')
    #extracting the datetimeIndex, converting it to np.array and then adding it to data
    new_array = data.index.strftime('%Y-%m-%d')
    data.insert(0, 'date', new_array)
    #converting data to excel, more readable
    data.to_excel(Path + 'RSI.xlsx', index = False)
    return ()



#This function returns the data from the NASDAQ every day
def getNASDAQ (Path):
    todayDate = datetime.date.today().strftime("%Y-%m-%d")
    data = yf.download("^IXIC", start= "2000-01-01", end = todayDate, interval = "1d")
    #extracting the datetimeIndex, converting it to np.array and then adding it to data
    new_array = data.index.strftime('%Y-%m-%d')
    data.insert(0, 'date', new_array)
    #converting data to excel, more readable
    data.to_excel(Path + 'NASDAQ.xlsx', index = False)
    return ()


#This function returns the data from the DOwJones every day
def getDOWJONES (Path):
    todayDate = datetime.date.today().strftime("%Y-%m-%d")
    data = yf.download("^DJI", start= "2000-01-01", end = todayDate, interval = "1d")
    #extracting the datetimeIndex, converting it to np.array and then adding it to data
    new_array = data.index.strftime('%Y-%m-%d')
    data.insert(0, 'date', new_array)
    #converting data to excel, more readable
    data.to_excel(Path + 'DOWJONES.xlsx', index = False)
    return ()


#This function returns the data from the SP500 every day
def getSP500(Path):
    todayDate = datetime.date.today().strftime("%Y-%m-%d")
    data = yf.download("^GSPC", start= "2000-01-01", end = todayDate, interval = "1d")
    #extracting the datetimeIndex, converting it to np.array and then adding it to data
    new_array = data.index.strftime('%Y-%m-%d')
    data.insert(0, 'date', new_array)
    #converting data to excel, more readable
    data.to_excel(Path + 'SP500.xlsx', index = False)
    return ()

#This function returns the data from the FTSE100 every day
def getFTSE100(Path):
    todayDate = datetime.date.today().strftime("%Y-%m-%d")
    data = yf.download("^FTSE", start= "2000-01-01", end = todayDate, interval = "1d")
    #extracting the datetimeIndex, converting it to np.array and then adding it to data
    new_array = data.index.strftime('%Y-%m-%d')
    data.insert(0, 'date', new_array)
    #converting data to excel, more readable
    data.to_excel(Path + 'FTSE100.xlsx', index = False)
    return ()

#This function returns the data from the DAX every day
def getDAX(Path):
    todayDate = datetime.date.today().strftime("%Y-%m-%d")
    data = yf.download("^GDAXI", start= "2000-01-01", end = todayDate, interval = "1d")
    #extracting the datetimeIndex, converting it to np.array and then adding it to data
    new_array = data.index.strftime('%Y-%m-%d')
    data.insert(0, 'date', new_array)
    #converting data to excel, more readable
    data.to_excel(Path + 'DAX.xlsx', index = False)
    return ()


#This function returns the data from the EUROSTOXX600 every day
def getSTOXX600(Path):
    todayDate = datetime.date.today().strftime("%Y-%m-%d")
    data = yf.download("^STOXX", start= "2000-01-01", end = todayDate, interval = "1d")
    #extracting the datetimeIndex, converting it to np.array and then adding it to data
    new_array = data.index.strftime('%Y-%m-%d')
    data.insert(0, 'date', new_array)
    #converting data to excel, more readable
    data.to_excel(Path + 'STOXX600.xlsx', index = False)
    return ()


#This function returns the data from the EUROSTOXX50 every day
def getSTOXX50E(Path):
    todayDate = datetime.date.today().strftime("%Y-%m-%d")
    data = yf.download("^STOXX50E", start= "2000-01-01", end = todayDate, interval = "1d")
    #extracting the datetimeIndex, converting it to np.array and then adding it to data
    new_array = data.index.strftime('%Y-%m-%d')
    data.insert(0, 'date', new_array)
    #converting data to excel, more readable
    data.to_excel(Path + 'STOXX50E.xlsx', index = False)
    return ()


#This function returns the data from the HSCEI every day
def getHSCEI(Path):
    todayDate = datetime.date.today().strftime("%Y-%m-%d")
    data = yf.download("^HSCE", start= "2000-01-01", end = todayDate, interval = "1d")
    #extracting the datetimeIndex, converting it to np.array and then adding it to data
    new_array = data.index.strftime('%Y-%m-%d')
    data.insert(0, 'date', new_array)
    #converting data to excel, more readable
    data.to_excel(Path + 'HSCEI.xlsx', index = False)
    return ()


#This function returns the data from the HSCEI every day
def getNIKKEI(Path):
    todayDate = datetime.date.today().strftime("%Y-%m-%d")
    data = yf.download("^N225", start= "2000-01-01", end = todayDate, interval = "1d")
    #extracting the datetimeIndex, converting it to np.array and then adding it to data
    new_array = data.index.strftime('%Y-%m-%d')
    data.insert(0, 'date', new_array)
    #converting data to excel, more readable
    data.to_excel(Path + 'NIKKEI.xlsx', index = False)
    return ()


#This function returns the data from the HSCEI every day
def getCAC40(Path):
    todayDate = datetime.date.today().strftime("%Y-%m-%d")
    data = yf.download("^FCHI", start= "2000-01-01", end = todayDate, interval = "1d")
    #extracting the datetimeIndex, converting it to np.array and then adding it to data
    new_array = data.index.strftime('%Y-%m-%d')
    data.insert(0, 'date', new_array)
    #converting data to excel, more readable
    data.to_excel(Path + 'CAC40.xlsx', index = False)
    return ()


#This function returns the data from the VIX every day
def getVIX(Path):
    todayDate = datetime.date.today().strftime("%Y-%m-%d")
    data = yf.download("^VIX", start= "2000-01-01", end = todayDate, interval = "1d")
    #extracting the datetimeIndex, converting it to np.array and then adding it to data
    new_array = data.index.strftime('%Y-%m-%d')
    data.insert(0, 'date', new_array)
    #converting data to excel, more readable
    data.to_excel(Path + 'VIX.xlsx', index = False)
    return ()


#This function returns the data from the DOLLAR INDEX every day
def getDOLLARINDEX(Path):
    todayDate = datetime.date.today().strftime("%Y-%m-%d")
    data = yf.download("DX-Y.NYB", start= "2000-01-01", end = todayDate, interval = "1d")
    #extracting the datetimeIndex, converting it to np.array and then adding it to data
    new_array = data.index.strftime('%Y-%m-%d')
    data.insert(0, 'date', new_array)
    #converting data to excel, more readable
    data.to_excel(Path + 'DOLLARINDEX.xlsx', index = False)
    return ()


#This function returns the data from the TAUX 10 US every day
def getTAUX10US(Path):
    todayDate = datetime.date.today().strftime("%Y-%m-%d")
    data = yf.download("^TNX", start= "2000-01-01", end = todayDate, interval = "1d")
    #extracting the datetimeIndex, converting it to np.array and then adding it to data
    new_array = data.index.strftime('%Y-%m-%d')
    data.insert(0, 'date', new_array)
    #converting data to excel, more readable
    data.to_excel(Path + 'TAUX10US.xlsx', index = False)
    return ()


#This function returns the data from the TAUX 5 US every day
def getTAUX5US(Path):
    todayDate = datetime.date.today().strftime("%Y-%m-%d")
    data = yf.download("^FVX", start= "2000-01-01", end = todayDate, interval = "1d")
    #extracting the datetimeIndex, converting it to np.array and then adding it to data
    new_array = data.index.strftime('%Y-%m-%d')
    data.insert(0, 'date', new_array)
    #converting data to excel, more readable
    data.to_excel(Path + 'TAUX5US.xlsx', index = False)
    return ()


#This function returns the data from the GOLD every day
def getGOLD(Path):
    todayDate = datetime.date.today().strftime("%Y-%m-%d")
    yahoo_financials_commodities = YahooFinancials('GC=F')
    data = yahoo_financials_commodities.get_historical_price_data('2000-01-01', todayDate, 'daily')
    new_array=[]
    for item in data['GC=F']['prices']:
        if item['open'] != '':
            Date = datetime.date.fromtimestamp(item['date']).strftime('%Y-%m-%d')
            new_array.append([Date,item['open']])
    #converting new_array to excel, more readable
    new_array = pd.DataFrame(new_array)
    new_array.to_excel(Path + 'GOLD.xlsx', index = False)
    return ()


#This function returns the data from the OIL every day
def getOIL(Path):
    todayDate = datetime.date.today().strftime("%Y-%m-%d")
    yahoo_financials_commodities = YahooFinancials('CL=F')
    data = yahoo_financials_commodities.get_historical_price_data('2000-01-01', todayDate, 'daily')
    new_array=[]
    for item in data['CL=F']['prices']:
        if item['open']:
            Date = datetime.date.fromtimestamp(item['date']).strftime('%Y-%m-%d')
            new_array.append([Date,item['open']])
    #converting new_array to excel, more readable
    new_array = pd.DataFrame(new_array)
    new_array.to_excel(Path + 'OIL.xlsx', index = False)
    return ()

#This function returns the data from the EURUSD every day
def getEURUSD(Path):
    todayDate = datetime.date.today().strftime("%Y-%m-%d")
    yahoo_financials_currencies = YahooFinancials('EURUSD=X')
    data = yahoo_financials_currencies.get_historical_price_data('2000-01-01', todayDate, 'daily')
    new_array=[]
    for item in data['EURUSD=X']['prices']:
        if item['open']:
            Date = datetime.date.fromtimestamp(item['date']).strftime('%Y-%m-%d')
            new_array.append([Date,item['open']])
    #converting new_array to excel, more readable
    new_array = pd.DataFrame(new_array)
    new_array.to_excel(Path + 'EURUSD.xlsx', index = False)
    return ()



#This function returns the data from the USDJPY every day
def getUSDJPY(Path):
    todayDate = datetime.date.today().strftime("%Y-%m-%d")
    yahoo_financials_currencies = YahooFinancials('USDJPY=X')
    data = yahoo_financials_currencies.get_historical_price_data('2000-01-01', todayDate, 'daily')
    new_array=[]
    for item in data['USDJPY=X']['prices']:
        if item['open']:
            Date = datetime.date.fromtimestamp(item['date']).strftime('%Y-%m-%d')
            new_array.append([Date,item['open']])
    #converting new_array to excel, more readable
    new_array = pd.DataFrame(new_array)
    new_array.to_excel(Path + 'USDJPY.xlsx', index = False)
    return ()



#This function returns the data from the USDCNY every day
def getUSDCNY(Path):
    todayDate = datetime.date.today().strftime("%Y-%m-%d")
    yahoo_financials_currencies = YahooFinancials('USDCNY=X')
    data = yahoo_financials_currencies.get_historical_price_data('2000-01-01', todayDate, 'daily')
    new_array=[]
    for item in data['USDCNY=X']['prices']:
        if item['open']:
            Date = datetime.date.fromtimestamp(item['date']).strftime('%Y-%m-%d')
            new_array.append([Date,item['open']])
    #converting new_array to excel, more readable
    new_array = pd.DataFrame(new_array)
    new_array.to_excel(Path + 'USDCNY.xlsx', index = False)
    return ()

