#CS175
#Lola Weis
#Stocks


commissionratepurchase=float(input("Enter commission rate percentage (ex 0.03) on stock purchase: "))
commissionratesale=float(input("Enter commission rate percentage (ex 0.03) on stock sale: "))
sharespurchased=float(input("Enter number of shares purchased: "))
sharessold=float(input("Enter number of shares sold: "))
purchaseprice=float(input("Enter purchase price per share: "))
sellprice=float(input("Enter sell price per share: "))


amountpaid=float(sharespurchased*purchaseprice)
print("Amount paid for the stock: $",(f'{amountpaid:,.2f}'))

commissionpaidpurchase=float(amountpaid*commissionratepurchase)
print("Commission paid on the purchase: $",(f'{commissionpaidpurchase:,.2f}'))

stocksoldfor=float(sharessold*sellprice)
print("Amount the stock sold for: $",(f'{stocksoldfor:,.2f}'))

commissionpaidsale=float(stocksoldfor*commissionratesale)
print("Commission paid on the sale: $",(f'{commissionpaidsale:,.2f}'))

totalpaid=float(amountpaid+commissionpaidpurchase+commissionpaidsale)
totalsold=float(stocksoldfor)
profitorloss=float(totalsold-totalpaid)
print("Profit (or loss if negative): $",(f'{profitorloss:,.2f}'))
