import yfinance as yf
import GetStockData
import StockStrtgy
# import pandas as pd
# import datetime

if __name__ == "__main__":
    Ticker = "SPY"
    StartDate = "2020-01-02"
    EndDate = "2021-01-02"

    InitFund = 100000

    StockData = GetStockData.GetStockHrData(Ticker, StartDate, EndDate)

    #buy and hold
    FinalFund1 = StockStrtgy.BuyHold(StockData, InitFund)
    print("Final Fund: {} dollars".format(FinalFund1))
    percentIncrease = ((FinalFund1 - InitFund) * 1.0 / InitFund) *100
    print("Percentage Increase: {:.2f}%".format(percentIncrease))