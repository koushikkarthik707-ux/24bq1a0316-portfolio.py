# Simple Stock Tracker

# Hardcoded dictionary of stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 320,
    "AMZN": 150
}

total_investment = 0
results = []

# Number of different stocks
n = int(input("Enter the number of stocks: "))

for i in range(n):
    stock_name = input("\nEnter stock name (AAPL, TSLA, GOOG, MSFT, AMZN): ").upper()
    quantity = int(input("Enter quantity: "))

    if stock_name in stock_prices:
        price = stock_prices[stock_name]
        investment = price * quantity
        total_investment += investment

        results.append(f"{stock_name},{quantity},{price},{investment}")

        print("Investment for", stock_name, "=", investment)
    else:
        print("Stock not found!")

print("\nTotal Investment Value = $", total_investment)

# Ask user to save the result
choice = input("\nDo you want to save the result? (yes/no): ").lower()

if choice == "yes":
    filename = input("Enter file name (example: stocks.csv or stocks.txt): ")

    with open(filename, "w") as file:
        file.write("Stock,Quantity,Price,Investment\n")
        for item in results:
            file.write(item + "\n")
        file.write(f"\nTotal Investment = ${total_investment}")

    print("Data saved successfully in", filename)
else:
    print("Result not saved.")