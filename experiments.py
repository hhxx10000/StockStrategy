def print_basic(data):
    res = data[list(data.keys())[-1]][0]["open"] / data[list(data.keys())[0]][-1]["close"] * kInitFund
    percentageIncrease = ((res - kInitFund) * 1.0 / kInitFund)*100
    print("1月1日买了一只拿着能够获得 %.0f 美元， 上涨了%.0f%%" % (res, percentageIncrease))

def is_morning_market_bearish(today_candles, percentage):
    return today_candles[1]["open"] < today_candles[0]["open"] * percentage /100.0

def is_morning_market_bullish(today_candles, percentage):
    return today_candles[1]["open"] > today_candles[0]["open"] * percentage /100.0

def is_yesterday_afternoon_market_bearish(yesterday_candles, percentage):
    return yesterday_candles[-1]["close"] < yesterday_candles[-4]["open"] * percentage /100.0

def is_afternoon_market_bullish(today_candles, percentage):
    return today_candles[-2]["open"] > today_candles[-4]["open"] * percentage /100.0

if __name__ == "__main__":
    ticker = "spy"
    volativity = 2
    print("本金10万美元")
    print("买卖对象 %s" % (ticker))
    # Process Ticker Data
    data = read_data(ticker)
    print_basic(data)
    #Experiment
    experiment(data, 20, 100+volativity, 100-volativity)
    percentIncrease = ((best_market_value - kInitFund) * 1.0 / kInitFund)*100
    # Result
    print("1月1日《傻瓜炒股心经》法则结果： %.0f 美元，上涨了%.0f%%" % (best_market_value, percentIncrease))
    print_pine_script("labels.pine")