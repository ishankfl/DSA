# best-time-to-buy-and-sell-stock
stocks_prices = [1000,500,200,100]
max_value=0
pos=0
for each in range(len(stocks_prices)):
    if stocks_prices[each] > max_value:
        max_value=stocks_prices[each]
        pos=each
print(pos,max_value)

min_value =max_value

for i in range(0,pos): 
    print(stocks_prices[i])
    if stocks_prices[i] < min_value:
        min_value = stocks_prices[i]
        continue
        
print(max_value,min_value)
print("MAX profit ", max_value-min_value)  
        
     