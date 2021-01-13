import yfinance as yf
import pandas as pd

def GetStockHrData(Ticker, StartDate, EndDate):
    Fulldata = yf.download(Ticker, StartDate, EndDate, interval = "60m")
    Fulldata.reset_index(inplace = True)
    
    data = pd.DataFrame(Fulldata[['Datetime', 'Open', 'Close']])
    data['StockDate'] = data['Datetime'].apply(lambda x: x.date())
    # data['StockTime'] = data['Datetime'].apply(lambda x: x.time())
    data.drop(columns = 'Datetime', inplace = True)
    g = data.groupby('StockDate')

    StockData = {'Open': [], 'Close': [], 'Date':[]}
    for IdvDate, df_hrStock in g:
        StockData['Open'].append(df_hrStock['Open'].tolist())
        StockData['Close'].append(df_hrStock['Close'].tolist())
        StockData['Date'].append(IdvDate)
    return StockData

if __name__ == "__main__":
    Ticker = "SPY"
    StartDate = "2020-01-02"
    EndDate = "2021-01-02"

    StockData = GetStockHrData(Ticker, StartDate, EndDate)
    print(StockData['Open'][0])
    print(StockData['Close'][-1])
    print(StockData['Date'][0])
