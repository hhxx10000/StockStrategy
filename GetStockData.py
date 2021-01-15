import yfinance as yf
import pandas as pd

def GetStockHrData(Ticker, StartDate, EndDate):
    Fulldata = yf.download(Ticker, StartDate, EndDate, interval = "60m")
    Fulldata.reset_index(inplace = True)
    
    data = pd.DataFrame(Fulldata[['Datetime', 'Open', 'Close']])
    data['StockDate'] = data['Datetime'].dt.date

    # data['StockTime'] = data['Datetime'].apply(lambda x: x.time())
    data.drop(columns = 'Datetime', inplace = True)
    titles = list(data.columns)
    titles[0], titles[1], titles[2] = titles[2], titles[0], titles[1]
    data = data[titles]
    
    grp = data.groupby('StockDate')
    StockDate = list(grp.groups.keys())

    StockData = []
    for iDay in StockDate:
        StockIntraday = grp.get_group(iDay)
        StockData.append(StockIntraday[['Open','Close']].to_dict('records'))
    return StockDate, StockData

if __name__ == "__main__":
    Ticker = "SPY"
    StartDate = "2020-01-02"
    EndDate = "2021-01-02"

    StockDate, StockData = GetStockHrData(Ticker, StartDate, EndDate)
    print(StockData[0][0]['Open'])
    print(StockDate[0])
    print(StockData[-1][-1]['Close'])
    print(StockDate[-1])

