#This is my Stock Prices (Using dictionaries {}):
stock_prices = {
    "APPL": 190,
    "AMZN" : 180 ,
    "SMSNG": 200 ,  
    "MSFT":  170 ,
    "TSLA": 250 ,
}

#Ask for the stock name:
stock_name = input("Enter the stock symbol or code:")
#Ask for the quantity they own:
Quantity = int(input("How many shares do you own?"))

#Now check and if the stock are in our price book and do calculation by using if-else condition:
if stock_name in stock_prices:
     
     price = stock_prices[stock_name]
     total = price * Quantity
     print(f"{stock_name}: shares{Quantity} * ${price} = ${total}")   #f string used to show in text form 

else:
     print("Sorry, I don't have a price for that stock.")

#Now using while loop for checking as much as they can and also for stop/finish:
portfolio_total=0
while True:
     stock_name =input(f"\nEnter stock symbol or name (or 'Done' to finish)")

     if stock_name == "Done":  
          break           #Stop the loop
     
     if stock_name in stock_prices:      #After check for break then do the math by using conditions:
          Quantity = int(input("How many shares do you own?"))
          price = stock_prices[stock_name]
          total = price * Quantity
          portfolio_total += total        #Add to running total
          print(f"{stock_name}: shares{ Quantity} * ${price} = ${total}")

     else:
          print("Stock not found! Avalaible: APPL,SMSNG,MSFT,TSLA,AMZN")

print(f"\n Your total portfolio value: ${portfolio_total}")






     
    