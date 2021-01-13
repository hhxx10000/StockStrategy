# define stock strategy

def BuyHold(StockData, OrigFund):
    startPrice = StockData['Open'][0][0]
    endPrice = StockData['Close'][-1][-1]
    return float(OrigFund)/startPrice*endPrice
