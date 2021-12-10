prices = [7,1,5,3,6,4]

def best_time_sell(prices):
    #If there is one value in the array return zero cant find the profit as we cant buy n sell in thesame day
    n = len(prices)
    if n < 2:
        return 0

    #Initalize maxprofit and minvalue
    maxProfit = 0
    minValue = prices[0]

    #Keeping track of maxprofit and min value
    for p in prices:
        maxProfit = max(maxProfit,p-minValue)
        minValue = min(p,minValue)
    print(maxProfit)

    #Return the maxProfit
    return maxProfit   

best_time_sell(prices)     