Python 3.10.7 (v3.10.7:7cc6b13308, Sep  5 2022, 14:02:52) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
commissionratepurchase=input(float("Enter commission rate percentage (ex 0.03) on stock purchase: "))
commissionratesale=input(float("Enter commission rate percentage (ex 0.03) on stock sale: "))
sharespurchased=input(float("Enter number of shares purchased: "))
sharessold=input(float("Enter number of shares sold: "))
purchaseprice=input(float("Enter purchase price per share: "))
sellprice=input(float("Enter sell price per share: "))


amountpaid=(sharespurchased*purchaseprice)
print("Amount paid for the stock: $",(f'{amountpaid:,.2f}')
