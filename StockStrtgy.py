import GetStockData

# define stock strategy
def BuyHold(StockDate, StockData, InitFund):
    startPrice = StockData[0][0]['Open']
    endPrice = StockData[-1][-1]['Close']
    return float(InitFund)/startPrice*endPrice

def LazyInvest(StockDate, StockData, InitFund):
    # 懒人炒股心经：
    #   早上大跌要加仓
    #   早上大涨要减仓
    #   下午大涨只减仓
    #   下午大跌次日买
    NumOfDay = len(StockData)
    HoldCash = [InitFund] + [0] * (NumOfDay)
    HoldStock = [0] * (NumOfDay + 1)
    percentage = 2.0
    BuyRatio = 0.2
    SellRatio = 0.2

    for iDay, iDate in enumerate(StockDate):
        if iDay > 0:
            yesterdayStock = StockData[iDay-1]
        else:
            yesterdayStock = StockData[iDay]
        todayStock = StockData[iDay]

        CurrCash = HoldCash[iDay]
        CurrNumStock = HoldStock[iDay]
        # 下午大跌次日买
        if is_yesterday_afternoon_market_bearish(yesterdayStock, 100.0 - percentage):
            # buy 20%
            currStockPrice = todayStock[0]['Open']
            TotalValue = currStockPrice*CurrNumStock+CurrCash
            if CurrCash > TotalValue * BuyRatio:
                CurrNumStock += (TotalValue * BuyRatio)//currStockPrice
                CurrCash -= currStockPrice * CurrNumStock
        
        # 早上大跌要加仓
        if is_morning_market_bearish(todayStock, 100.0 - percentage):
            # buy 20%
            currStockPrice = todayStock[1]["Open"]
            TotalValue = currStockPrice*CurrNumStock+CurrCash
            if CurrCash > TotalValue * BuyRatio:
                CurrNumStock += (TotalValue * BuyRatio)//currStockPrice
                CurrCash -= currStockPrice * CurrNumStock
        
        # 早上大涨要减仓
        if is_morning_market_bullish(todayStock, 100.0 + percentage):
            # sell 20%
            currStockPrice = todayStock[1]["Open"]
            TotalValue = currStockPrice*CurrNumStock+CurrCash
            if CurrNumStock * currStockPrice > TotalValue * SellRatio:
                CurrNumStock -= (TotalValue * SellRatio)//currStockPrice
                CurrCash += currStockPrice * CurrNumStock
        # 下午大涨只减仓
        if is_afternoon_market_bullish(todayStock, 100.0 + percentage):
            # sell 20%
            currStockPrice = todayStock[-2]["Open"]
            TotalValue = currStockPrice*CurrNumStock+CurrCash
            if CurrNumStock * currStockPrice > TotalValue * SellRatio:
                CurrNumStock -= (TotalValue * SellRatio)//currStockPrice
                CurrCash += currStockPrice * CurrNumStock
        HoldCash[iDay + 1] = CurrCash
        HoldStock[iDay + 1] = CurrNumStock
        print(CurrCash, CurrNumStock)
    print(HoldCash[-1], HoldStock[-1])
    return

def is_morning_market_bearish(today_candles, percentage):
    return today_candles[1]["Open"] < today_candles[0]["Open"] * percentage /100.0

def is_morning_market_bullish(today_candles, percentage):
    return today_candles[1]["Open"] > today_candles[0]["Open"] * percentage /100.0

def is_yesterday_afternoon_market_bearish(yesterday_candles, percentage):
    return yesterday_candles[-1]["Close"] < yesterday_candles[-4]["Open"] * percentage /100.0

def is_afternoon_market_bullish(today_candles, percentage):
    return today_candles[-2]["Open"] > today_candles[-4]["Open"] * percentage /100.0

if __name__ == "__main__":
    Ticker = "SPY"
    StartDate = "2020-01-02"
    EndDate = "2021-01-02"
    StockDate, StockData = GetStockData.GetStockHrData(Ticker, StartDate, EndDate)
    LazyInvest(StockDate, StockData, 100000)