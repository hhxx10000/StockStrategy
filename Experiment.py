import yfinance as yf

def readData(ticker, startDate, endDate):
    rawData = yf.download(ticker, startDate, endDate, interval = "60m")
    #convert data frame data to dictionary
    DictData = rawData.to_dict('index')
    return DictData


if __name__ == "__main__":
    # Testing Range
    test_start_time = "2019-01-10"
    test_end_time = "2020-12-31"

    ## Account Settings
    print("本金10万美元")
    available_fund = 100000
    total_fund = 100000
    num_shares = 0
    account_dict = {}

    #criteria
    ticker = "QQQ"
    print("买卖对象 %s" % (ticker))
    Volatility = 0.02
    BuyPortion = 0.4

    #Process Ticker Data
    data = readData(ticker, test_start_time, test_end_time)
    print(data.keys())
    #print_basic(data)

    #Experiment
    # experiment(data, 20, 100+volatility, 100-volatility)
    # percentIncrease = ((best_market_value - kInitFund) * 1.0 / kInitFund) *100

    # #Result
    # print("1月1日《傻瓜炒股心经》结果： %.0f 美元，上涨了%.0f%%" % (best_market_value, percentIncrease))


#     def zeroX(n):
#     result = ""
#     if (n < 10):
#         result += "0"
#     result += str (n)
#     return result

# def dump_Pandas_Timestamp (ts):
#     result = ""
#     result += str(ts.year) + "-" + zeroX(ts.month) + "-" + zeroX(ts.day)
#     #result += " " + zeroX(ts.hour) + ":" + zeroX(ts.minute) + ":" + zeroX(ts.second)
#     return result

# def dump_Pandas_DataFrame (DF):
#     result = ""
#     for indexItem in DF.index:
#         ts = dump_Pandas_Timestamp (indexItem)
#         fields = ""
#         first = 1
#         for colname in DF.columns:
#             fields += ("" if first else ", ") + colname + " = " + str(DF[colname][indexItem])
#             first = 0
#         result += ts + " " + fields + "\n"
#     return result
    
# msft = yf.Ticker("MSFT")
    
# # get historical market data
# hist = msft.history(period="1mo", interval="1d")
    
# print ("hist = " + dump_Pandas_DataFrame(hist))