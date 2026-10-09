import csv 
from datetime import datetime

# STOCK DATABASE
stock_prices = {
    "AAPL": 190.00,
    "TSLA": 840.00, 
    "MSFT": 300.00,
    "AMZN": 140.00,
    "NVDA": 400.00,
    "META": 330.00
}

# DISPLAY AVAILABLE STOCKS

def show_available_stocks():

    print("\nAvailable Stocks")
    print("-" * 35)

    for symbol, price in stock_prices.items():
        print(f"{symbol:<8} ${price:>8.2f}")

    print("-" * 35)



# ADD STOCK TO PORTFOLIO
def add_stock(portfolio):

    symbol = input("\nEnter stock symbol: ").upper().strip()

    # check whether stock exists
    if symbol not in stock_prices:
        print("Stock is not available.")
        return

    try:
        quantity = int(input("Enter quantity:"))
        if quantity <= 0:
            print("Quantity must be a positive integer.")
            return

    except ValueError:
        print("Invalid input. Please enter a valid integer for quantity.")
        return

    # If stock already exists , increase quantity
    if symbol in portfolio:
        portfolio[symbol] += quantity
    else:
        portfolio[symbol] = quantity

    print(f"{quantity} shares of {symbol} added successfully.")


# CALCULATE PORTFOLIO 

def calculate_portfolio(portfolio):
    portfolio_data = []
    total_value = 0

    for symbol, quantity in portfolio.items():
        price = stock_prices[symbol]
        investment = price * quantity
        total_value += investment

        portfolio_data.append({
            "symbol": symbol,
            "quantity": quantity,
            "price": price,
            "investment": investment
        })

# CALCULATE PERCENTAGE
    
    for stock in portfolio_data:

        if total_value < 0:
            stock["percentage"] = (stock["investment"] / total_value) * 100

        else:
            stock["percentage"] = 0

    return portfolio_data, total_value            

# DISPLAY PORTFOLIO

def display_portfolio(portfolio):

    if not portfolio:
        print("\nYour portfolio is empty.")
        return

    data, total_value = calculate_portfolio(portfolio)

    print("\n")
    print("-" * 60)
    print("                STOCK PORTFOLIO") 
    print("-" * 60)

    print(
        f"{'Stock':<10}"
        f"{'Quantity':<12}"
        f"{'Price':<15}"
        f"{'Investment':<18}"
        f"{'Weight':<10}"
    )

    print("-" * 60)

    for stock in data:

        print(
            f"{stock['symbol']:<10}"
            f"{stock['quantity']:<12}"
            f"${stock['price']:<14.2f}"
            f"${stock['investment']:<17.2f}"
            f"{stock['percentage']:.2f}%"
        )       

    print("-" * 60)

    print(f"TOTAL PORTFOLIO VALUE: ${total_value:,.2f}")

    print("-" * 60)

# SAVE PORTFOLIO TO CSV

def save_to_csv(portfolio):
    if not portfolio:
        print("\nPortfolio is empty. Nothing to save.")
        return

    data, total_value = calculate_portfolio(portfolio)

    filename = "stock_portfolio.csv"

    with open(filename, "w", newline = "") as file:
        writer = csv.writer(file)
        writer.writerow([
            "Stock",
            "Quantity",
            "Price",
            "Investment",
            "Portfolio Weight"
    ])

        for stock in data:
            writer.writerow([
                stock["symbol"],
                stock["quantity"],
                stock["price"],
                stock["investment"],
                f"{stock['percentage']:.2f}"
            ])

        writer.writerow([])
        writer.writerow(["Total Portfolio Value", total_value])  
    print(f"\nPortfolio saved to {filename} successfully.")

# SAVE PORTFOLIO TO TEXT

def save_to_txt(portfolio):
    if not portfolio:
        print("\nPortfolio is empty, Nothing to save.")
        return

    data, total_value = calculate_portfolio(portfolio)

    filename = "stock_portfolio.txt"

    with open(filename, "w") as file:

        file.write("=" * 60 + "\n")
        file.write("            STOCK PORTFOLIO REPORT\n")
        file.write("=" * 60 + "\n")

        file.write(
            f"Genearated: "
            f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
        )

        for stock in data:

            file.write(
                f"Stock: {stock['symbol']}\n"
                f"Quantity: {stock['quantity']}\n"
                f"Price: ${stock['price']:.2f}\n"
                f"Investment: ${stock['investment']:.2f}\n"
                f"Portfolio weight: {stock['percentage']:.2f}%\n"
            )

            file.write("=" * 60 + "\n")
        file.write(
            f"\nTOTAL PORTFOLIO VALUE: ${total_value:,.2f}\n"
        )

        file.write("=" * 60 + "\n")

    print(f"\nPortfolio saved successfully to {filename}.")

# MAIN FUNCTION

def main():
    portfolio = {}

    print("-" * 50)
    print("     STOCK PORTFOLIO TRACKER")
    print("-" * 50)

    while True:

        print("\n Menu: ")
        print("1. Show available stocks")
        print("2. Add stock")
        print("3. View portfolio")
        print("4. Save portfolio to CSV")
        print("5. Save portfolio to TXT")
        print("6. Exit")
        print("----------------------------")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            show_available_stocks()

        elif choice == "2":
            add_stock(portfolio)

        elif choice == "3": 
            display_portfolio(portfolio)

        elif choice == "4":
            save_to_csv(portfolio)

        elif choice == "5":
            save_to_txt(portfolio)

        elif choice == "6":
            print("\n THANK FOR USING STOCK PORTFOLIO TRACKER!!!")
            break

        else:
            print("Invalid choice. Please select 1-6.")

# START POROGRAM
if __name__ == "__main__":
    main()




