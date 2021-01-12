import yfinance as yf
# import pandas as pd
# import datetime

if __name__ == "__main__":
    Ticker = "SPY"
    Fulldata = yf.download(Ticker, start="2020-01-02", end="2021-01-02", interval = "60m")
    Fulldata.reset_index(inplace = True)
    
    data = Fulldata[['Datetime', 'Open', 'Close']]
    data['StockDate'] = data['Datetime'].apply(lambda x: x.date())
    data['StockTime'] = data['Datetime'].apply(lambda x: x.time())
    data.drop(columns = 'Datetime', inplace = True)
    g = data.groupby('StockDate')

    StockData = {'Open': [], 'Close': [], 'Date':[]}
    for IdvDate, df_hrStock in g:
        StockData['Open'].append(df_hrStock['Open'].tolist())
        StockData['Close'].append(df_hrStock['Close'].tolist())
        StockData['Date'].append(IdvDate)

    
    # print(StockData['Open'])
    # print(StockData['Close'])
    # print(StockData['Date'])
        # print(IdvDate)
        # print(datetime.datetime.strptime("2020-01-10", '%Y-%m-%d'))
        # if IdvDate > datetime.datetime.strptime("2020-12-23", '%Y-%m-%d').date():
        #     print(IdvDate)
        #     print(df_hrStock)

    # print(data.head(20))
    # print(int(data['Open'].count()/5))
    # print(OpenPrice)



    # StockDate = data['Datetime'].apply(lambda x: x.date())
    # StockTime = data['Datetime'].apply(lambda x: x.time())
    # #print(type(StockDate))
    # print(StockTime[1])

    # StockData = []
    # for idx, date in enumerate(StockDate):