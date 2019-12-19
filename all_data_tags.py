#!/usr/bin/env python
# coding: utf-8

# In[84]:


from __future__ import print_function
import time
import intrinio_sdk
import json
import requests
import pandas as pd

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'OmNhZTYyZjhlZTc4MTc5MTg5ZTMzYzg1NTYzZGJhOWZj'

company_api = intrinio_sdk.CompanyApi()

identifier = 'AAPL'  # str | $$v2_company_historical_data_identifier_description$$
tag = 'marketcap'  # str | $$v2_company_historical_data_item_description$$
frequency = 'daily'  # str | Return historical data in the given frequency (optional) (default to daily)
type = ''  # str | Filter by type, when applicable (optional)
start_date = '2008-01-01'  # date | Get historical data on or after this date (optional)
end_date = '2019-01-01'  # date | Get historical data on or before this date (optional)
sort_order = 'desc'  # str | Sort by date `asc` or `desc` (optional) (default to desc)
page_size = 10000  # float | The number of results to return (optional) (default to 100)
next_page = ''  # str | Gets the next page of data from a previous API call (optional)
response = requests.get(
    'https://api-v2.intrinio.com/companies/AAPL/historical_data/marketcap?api_key=OmNhZTYyZjhlZTc4MTc5MTg5ZTMzYzg1NTYzZGJhOWZj&start_date=2008-01-01&end_date=2019-03-31&page_size=10000')


#marketCap data
data = response.json()['historical_data']
#print(data)
json.dumps(data)
dfMarketCap = pd.DataFrame(data)
dfMarketCap.columns=['Date','MarketCap']
dfMarketCap= dfMarketCap.set_index('Date')
#dfMarketCap.to_csv('marketCap.csv')
print(dfMarketCap)
time.sleep(120)


#DebtToEquity - 38
# responseDebtEquity = requests.get(
#     'https://api-v2.intrinio.com/companies/AAPL/historical_data/debttoequity?api_key=OmNhZTYyZjhlZTc4MTc5MTg5ZTMzYzg1NTYzZGJhOWZj&start_date=2008-01-01&end_date=2019-03-31&page_size=10000')
# dataDebtToEquity = responseDebtEquity.json()
# #print(dataDebtToEquity)
# histDebtToEquity = dataDebtToEquity['historical_data']
# #print(histDebtToEquity)
# json.dumps(histDebtToEquity)
# dfDebtToEquity = pd.DataFrame(histDebtToEquity)
# dfDebtToEquity.columns=['Date','DebtToEquity']
# dfDebtToEquity= dfDebtToEquity.set_index('Date')
# print(dfDebtToEquity)
# time.sleep(120)


#PriceToBooknan
# responsePriceToBook = requests.get(
#     'https://api-v2.intrinio.com/companies/AAPL/historical_data/pricetobook?api_key=OmNhZTYyZjhlZTc4MTc5MTg5ZTMzYzg1NTYzZGJhOWZj&start_date=2008-01-01&end_date=2019-03-31&page_size=10000')
# dataPriceToBook = responsePriceToBook.json()
# #print(dataPriceToBook)
# json.dumps(dataPriceToBook)
# histPriceToBook = dataPriceToBook['historical_data']
# #print(histPriceToBook)
# dfPriceToBook = pd.DataFrame(histPriceToBook)
# dfPriceToBook.columns=['Date','PriceToBook']
# dfPriceToBook= dfPriceToBook.set_index('Date')
# print(dfPriceToBook)
# time.sleep(60)



#EVToRevenuenan
# responseEVToRevenue = requests.get(
#     'https://api-v2.intrinio.com/companies/AAPL/historical_data/evtorevenue?api_key=OmNlODdjMDI5MTlkNWEzNjRkOTYyN2JlZDc2ZTdhZTJh&start_date=2008-01-01&end_date=2019-03-31&page_size=10000')
# dataEVToRevenue = responseEVToRevenue.json()
# #print(dataEVToRevenue)
# histEVTORevenue = dataEVToRevenue['historical_data']
# #print(histEVTORevenue)
# json.dumps(histEVTORevenue)
# dfEVToRevenue = pd.DataFrame(histEVTORevenue)
# dfEVToRevenue.columns=['Date','EVToRevenue']
# dfEVToRevenue= dfEVToRevenue.set_index('Date')
# print(dfEVToRevenue)
# time.sleep(60)


#EVToEbitdanan
# responseEVToEbitda = requests.get(
#     'https://api-v2.intrinio.com/companies/AAPL/historical_data/evtoebitda?api_key=OmNlODdjMDI5MTlkNWEzNjRkOTYyN2JlZDc2ZTdhZTJh&start_date=2008-01-01&end_date=2019-03-31&page_size=10000')
# dataEVToEbitda = responseEVToEbitda.json()
# #print(dataEVToEbitda)
# histEVToEbitda = dataEVToEbitda['historical_data']
# #print(histEVToEbitda)
# json.dumps(histEVToEbitda)
# dfEVToEbitda = pd.DataFrame(histEVToEbitda)
# dfEVToEbitda.columns=['Date','EVToEbitda']
# dfEVToEbitda= dfEVToEbitda.set_index('Date')
# print(dfEVToEbitda)
# time.sleep(60)


#AdjustedVolume
responseAdjustedVolume = requests.get(
        'https://api-v2.intrinio.com/companies/AAPL/historical_data/adj_volume?api_key=OmNhZTYyZjhlZTc4MTc5MTg5ZTMzYzg1NTYzZGJhOWZj&start_date=2008-01-01&end_date=2019-03-31&page_size=10000')
jsonAdjustedVolume = responseAdjustedVolume.json()
#print(jsonAdjustedVolume)
histAdjustedVolume = jsonAdjustedVolume['historical_data']
#print(histAdjustedVolume)
json.dumps(histAdjustedVolume)
dfAdjustedVolume = pd.DataFrame(histAdjustedVolume)
dfAdjustedVolume.columns=['Date','AdjustedVolume']
dfAdjustedVolume= dfAdjustedVolume.set_index('Date')
#dfAdjustedVolume.to_csv('AdjustedVolume.csv')
print(dfAdjustedVolume)
time.sleep(60)


#AdjustedOpenPrice
responseAdjustedOpenPrice = requests.get(
        'https://api-v2.intrinio.com/companies/AAPL/historical_data/adj_open_price?api_key=OmNhZTYyZjhlZTc4MTc5MTg5ZTMzYzg1NTYzZGJhOWZj&start_date=2008-01-01&end_date=2019-03-31&page_size=10000')
jsonAdjustedOpenPrice = responseAdjustedOpenPrice.json()
#print(jsonAdjustedOpenPrice)
histAdjustedOpenPrice = jsonAdjustedOpenPrice['historical_data']
#print(histAdjustedOpenPrice)
json.dumps(histAdjustedOpenPrice)
dfAdjustedOpenPrice = pd.DataFrame(histAdjustedOpenPrice)
dfAdjustedOpenPrice.columns=['Date','AdjustedOpenPrice']
dfAdjustedOpenPrice= dfAdjustedOpenPrice.set_index('Date')
#dfAdjustedOpenPrice.to_csv('AdjustedOpenPrice.csv')
print(dfAdjustedOpenPrice)
time.sleep(60)


#AdjustedLowPrice
responseAdjustedLowPrice = requests.get(
        'https://api-v2.intrinio.com/companies/AAPL/historical_data/adj_low_price?api_key=OmNhZTYyZjhlZTc4MTc5MTg5ZTMzYzg1NTYzZGJhOWZj&start_date=2008-01-01&end_date=2019-03-31&page_size=10000')
jsonAdjustedLowPrice = responseAdjustedLowPrice.json()
#print(jsonAdjustedLowPrice)
histAdjustedLowPrice = jsonAdjustedLowPrice['historical_data']
#print(histAdjustedLowPrice)
json.dumps(histAdjustedLowPrice)
dfAdjustedLowPrice = pd.DataFrame(histAdjustedLowPrice)
dfAdjustedLowPrice.columns=['Date','AdjustedLowPrice']
dfAdjustedLowPrice= dfAdjustedLowPrice.set_index('Date')
#dfAdjustedLowPrice.to_csv('AdjustedLowPrice.csv')
print(dfAdjustedLowPrice)
time.sleep(60)


#AdjustedHighPrice
responseAdjustedHighPrice = requests.get(
        'https://api-v2.intrinio.com/companies/AAPL/historical_data/adj_high_price?api_key=OmNhZTYyZjhlZTc4MTc5MTg5ZTMzYzg1NTYzZGJhOWZj&start_date=2008-01-01&end_date=2019-03-31&page_size=10000')
jsonAdjustedHighPrice = responseAdjustedHighPrice.json()
#print(jsonAdjustedHighPrice)
histAdjustedHighPrice = jsonAdjustedHighPrice['historical_data']
#print(histAdjustedHighPrice)
json.dumps(histAdjustedHighPrice)
dfAdjustedHighPrice = pd.DataFrame(histAdjustedHighPrice)
dfAdjustedHighPrice.columns=['Date','AdjustedHighPrice']
dfAdjustedHighPrice= dfAdjustedHighPrice.set_index('Date')
#dfAdjustedHighPrice.to_csv('AdjustedHighPrice.csv')
print(dfAdjustedHighPrice)
time.sleep(60)


#AdjustedClosePrice
responseAdjustedClosePrice = requests.get(
        'https://api-v2.intrinio.com/companies/AAPL/historical_data/adj_close_price?api_key=OmNhZTYyZjhlZTc4MTc5MTg5ZTMzYzg1NTYzZGJhOWZj&start_date=2008-01-01&end_date=2019-03-31&page_size=10000')
jsonAdjustedClosePrice = responseAdjustedClosePrice.json()
#print(jsonAdjustedClosePrice)
histAdjustedClosePrice = jsonAdjustedClosePrice['historical_data']
#print(histAdjustedClosePrice)
json.dumps(histAdjustedClosePrice)
dfAdjustedClosePrice = pd.DataFrame(histAdjustedClosePrice)
dfAdjustedClosePrice.columns=['Date','AdjustedClosePrice']
dfAdjustedClosePrice= dfAdjustedClosePrice.set_index('Date')
#dfAdjustedClosePrice.to_csv('AdjustedClosePrice.csv')
print(dfAdjustedClosePrice)
time.sleep(60)

#Volume
responseVolume = requests.get(
        'https://api-v2.intrinio.com/companies/AAPL/historical_data/volume?api_key=OmNhZTYyZjhlZTc4MTc5MTg5ZTMzYzg1NTYzZGJhOWZj&start_date=2008-01-01&end_date=2019-03-31&page_size=10000')
jsonVolume = responseVolume.json()
#print(jsonVolume)
histVolume = jsonVolume['historical_data']
#print(histVolume)
json.dumps(histVolume)
dfVolume = pd.DataFrame(histVolume)
dfVolume.columns=['Date','Volume']
dfVolume= dfVolume.set_index('Date')
#dfVolume.to_csv('Volume.csv')
print(dfVolume)
time.sleep(60)



#ClosePrice
responseClosePrice = requests.get(
        'https://api-v2.intrinio.com/companies/AAPL/historical_data/close_price?api_key=OmNhZTYyZjhlZTc4MTc5MTg5ZTMzYzg1NTYzZGJhOWZj&start_date=2008-01-01&end_date=2019-03-31&page_size=10000')
jsonClosePrice = responseClosePrice.json()
#print(jsonClosePrice)
histClosePrice = jsonClosePrice['historical_data']
#print(histClosePrice)
json.dumps(histClosePrice)
dfClosePrice = pd.DataFrame(histClosePrice)
dfClosePrice.columns=['Date','ClosePrice']
dfClosePrice= dfClosePrice.set_index('Date')
#dfClosePrice.to_csv('ClosePrice.csv')
print(dfClosePrice)
time.sleep(60)


#OpenPrice
responseOpenPrice = requests.get(
        'https://api-v2.intrinio.com/companies/AAPL/historical_data/open_price?api_key=OmNhZTYyZjhlZTc4MTc5MTg5ZTMzYzg1NTYzZGJhOWZj&start_date=2008-01-01&end_date=2019-03-31&page_size=10000')
jsonOpenPrice = responseOpenPrice.json()
#print(jsonOpenPrice)
histOpenPrice = jsonOpenPrice['historical_data']
#print(histOpenPrice)
json.dumps(histOpenPrice)
dfOpenPrice = pd.DataFrame(histOpenPrice)
dfOpenPrice.columns=['Date','OpenPrice']
dfOpenPrice= dfOpenPrice.set_index('Date')
#dfOpenPrice.to_csv('OpenPrice.csv')
print(dfOpenPrice)
time.sleep(60)


#LowPrice
responseLowPrice = requests.get(
        'https://api-v2.intrinio.com/companies/AAPL/historical_data/low_price?api_key=OmNhZTYyZjhlZTc4MTc5MTg5ZTMzYzg1NTYzZGJhOWZj&start_date=2008-01-01&end_date=2019-03-31&page_size=10000')
jsonLowPrice = responseLowPrice.json()
#print(jsonLowPrice)
histLowPrice = jsonLowPrice['historical_data']
#print(histLowPrice)
json.dumps(histLowPrice)
dfLowPrice = pd.DataFrame(histLowPrice)
dfLowPrice.columns=['Date','LowPrice']
dfLowPrice= dfLowPrice.set_index('Date')
#dfLowPrice.to_csv('LowPrice.csv')
print(dfLowPrice)
time.sleep(60)


#HighPrice
responseHighPrice = requests.get(
        'https://api-v2.intrinio.com/companies/AAPL/historical_data/high_price?api_key=OmNhZTYyZjhlZTc4MTc5MTg5ZTMzYzg1NTYzZGJhOWZj&start_date=2008-01-01&end_date=2019-03-31&page_size=10000')
jsonHighPrice = responseHighPrice.json()
#print(jsonHighPrice)
histHighPrice = jsonHighPrice['historical_data']
#print(histHighPrice)
json.dumps(histHighPrice)
dfHighPrice = pd.DataFrame(histHighPrice)
dfHighPrice.columns=['Date','HighPrice']
dfHighPrice= dfHighPrice.set_index('Date')
#dfHighPrice.to_csv('HighPrice.csv')
print(dfHighPrice)
time.sleep(60)

result = pd.concat([dfAdjustedVolume, dfMarketCap,dfAdjustedOpenPrice,dfAdjustedLowPrice,dfAdjustedHighPrice,dfAdjustedClosePrice,dfVolume
                    ,dfClosePrice,dfOpenPrice,dfLowPrice,dfHighPrice], axis=1, sort=False)
result.to_csv('final.csv')
