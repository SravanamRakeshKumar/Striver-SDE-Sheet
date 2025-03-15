def maxProfit(prices): #take prices as a Parameter
      buy_value=prices[0] #default buy and sell value is list[0]
      profit=0 #initially profit is zero
      for i in range(len(prices)):
        buy_value=min(buy_value,prices[i]) #find minimun price in the product for more profit
        profit=max(profit,prices[i]-buy_value) if (buy_value < prices[i]) else profit 
        #if selling cost is greater than the buying cost then profit ,otherwise lose. and compare to privious profit for find more profit of the product
      return profit
print(maxProfit([7,1,5,3,6,4])) #give prices as a Argument to the maxProfit function



        