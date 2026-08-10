stock_list={
    "AAPL":180,
    "TSLA":250,
    "GOOGL":150,
    "MSFT":140,
    "AMZN":160,
}


stk=input("Enter stock symbol").upper
stk_quantity=int(input("Enter the Quantity\n"))


if stk in stock_list:
    price=stock_list[stk]
    total=price*stk_quantity

    print("The Stock Portfolio Summary is:")
    print("Stock Symbol is:",stk)
    print("Price Per Share..in ..USD",price)
    print("Quantity..of stock..is",stk_quantity)
    print("Total Investment share..is",total)
    print("Total Investment:",total)

else:
    print("You Entered a wrong symbol for Stock...please enter a valid symbol")