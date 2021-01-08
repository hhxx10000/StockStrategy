import yfinance as yf

def GetStock(StockName, startDate, endDate, StockInterval):
    data = yf.download(tickers = StockName, start = startDate, end = endDate, interval = StockInterval)
    return data

if __name__ == "__main__":
    StockName = "SPY"
    startDate = "2020-01-01"
    endDate = "2020-12-31"
    StockInterval = "60m"
    data = GetStock(StockName, startDate, endDate, StockInterval)
    FirstDate = data.index[0]
    print(data.head(10))
    # print(FirstDate)
    # print(FirstDate.year)
    # print(FirstDate.month)
    # print(FirstDate.day)
    # print(FirstDate.hour)
    # print(FirstDate.minute)
    # print(FirstDate.second)
    # print(FirstDate.microsecond)
    # print(FirstDate.tzinfo)
