print("STOCK PORTFOLIO TRACKER")

stocks = {
    "TCS": 3500,
    "INFOSYS": 1800,
    "WIPRO": 500,
    "HCL": 1500,
    "APPLE": 200
}

total = 0

n = int(input("Enter number of stocks: "))

for i in range(n):

    name = input("Enter stock name: ").upper()

    if name in stocks:

        quantity = int(input("Enter quantity: "))

        price = stocks[name]

        amount = price * quantity

        total = total + amount

        print("Stock Name:", name)
        print("Stock Price:", price)
        print("Quantity:", quantity)
        print("Total Amount:", amount)

    else:
        print("Stock not available")

print("-------------------------")
print("Total Investment:", total)
print("Thank you!")
