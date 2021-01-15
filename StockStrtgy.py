import GetStockData

# define stock strategy
def BuyHold(StockDate, StockData, OrigFund):
    startPrice = StockData[0][0]['Open']
    endPrice = StockData[-1][-1]['Close']
    return float(OrigFund)/startPrice*endPrice

def LazyInvest(StockDate, StockData, InitFund):
    # 懒人炒股心经：
    #   早上大跌要加仓
    #   早上大涨要减仓
    #   下午大涨只减仓
    #   下午大跌次日买
    CurrCash = InitFund
    CurrStock = 0

    yesterday_candles = []
    for iDay, iDate in enumerate(StockDate):
        todayStock = 1
    print(InitCash, InitStock, TotalTime)

def is_morning_market_bearish(today_candles, percentage):
    return today_candles[1]["open"] < today_candles[0]["open"] * percentage /100.0

def is_morning_market_bullish(today_candles, percentage):
    return today_candles[1]["open"] > today_candles[0]["open"] * percentage /100.0

def is_yesterday_afternoon_market_bearish(yesterday_candles, percentage):
    return yesterday_candles[-1]["close"] < yesterday_candles[-4]["open"] * percentage /100.0

def is_afternoon_market_bullish(today_candles, percentage):
    return today_candles[-2]["open"] > today_candles[-4]["open"] * percentage /100.0

if __name__ == "__main__":
    Ticker = "SPY"
    StartDate = "2020-01-02"
    EndDate = "2021-01-02"
    StockData = GetStockData.GetStockHrData(Ticker, StartDate, EndDate)
    LazyInvest(StockData, 100000)