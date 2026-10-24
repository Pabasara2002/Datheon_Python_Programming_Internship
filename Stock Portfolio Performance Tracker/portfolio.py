import csv
import os
import random

def load_sp500_symbols(filename="constituents.csv"):
    """Loads valid ticker symbols from the S&P 500 CSV dataset."""
    symbols = set()
    if os.path.exists(filename):
        try:
            with open(filename, mode="r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    if "Symbol" in row:
                        symbols.add(row["Symbol"].strip().upper())
        except Exception as e:
            print(f"⚠️ Error reading {filename}: {e}")
    # Fallback default symbols if file is missing/unreadable
    return symbols if symbols else {"AAPL", "MSFT", "GOOGL", "AMZN", "TSLA", "MMM", "ABT"}

def get_current_price(ticker):
    """
    Simulates fetching current market price or can be extended with yfinance/requests.
    For demonstration, generates a realistic price or baseline mock price.
    """
    # Setting a random pseudo-market price based on ticker hash for consistency
    random.seed(ticker)
    return round(random.uniform(50.0, 500.0), 2)

def track_portfolio():
    print("==================================================")
    print("   DATHEON INVESTMENT PORTFOLIO TRACKING UTILITY  ")
    print("==================================================")
    
    valid_symbols = load_sp500_symbols()
    portfolio = {}

    print(f"Loaded {len(valid_symbols)} valid stock symbols from S&P 500 dataset.")
    print("\nEnter your holdings. Type 'done' when finished.\n")

    while True:
        ticker = input("Enter Stock Ticker Symbol (e.g., AAPL, MMM): ").strip().upper()
        if ticker == 'DONE':
            break
        
        if valid_symbols and ticker not in valid_symbols:
            confirm = input(f"⚠️ '{ticker}' is not found in the standard S&P 500 list. Do you still want to add it? (y/n): ").strip().lower()
            if confirm != 'y':
                continue

        try:
            buy_price = float(input(f"Enter Buy Price for {ticker} ($): "))
            quantity = float(input(f"Enter Share Quantity for {ticker}: "))
            
            if buy_price <= 0 or quantity <= 0:
                print("⚠️ Price and quantity must be greater than zero.")
                continue
                
            portfolio[ticker] = {
                "buy_price": buy_price,
                "quantity": quantity
            }
            print(f"✅ Successfully added {quantity} shares of {ticker} at ${buy_price:.2f}.\n")
        
        except ValueError:
            print("⚠️ Invalid numeric input. Please enter valid numbers for price and quantity.\n")

    if not portfolio:
        print("ℹ️ No holdings entered. Exiting program.")
        return

    # Process and calculate metrics
    summary_data = []
    total_invested = 0.0
    total_market_value = 0.0

    print("\n" + "="*75)
    print(f"{'TICKER':<10} | {'SHARES':<8} | {'BUY PRICE':<10} | {'CURR PRICE':<10} | {'INVESTED':<12} | {'VALUATION':<12} | {'GAIN/LOSS %':<10}")
    print("-" * 75)

    for ticker, data in portfolio.items():
        shares = data["quantity"]
        buy_price = data["buy_price"]
        curr_price = get_current_price(ticker)
        
        invested_capital = shares * buy_price
        market_val = shares * curr_price
        gain_loss_pct = ((curr_price - buy_price) / buy_price) * 100

        total_invested += invested_capital
        total_market_value += market_val

        summary_data.append({
            "Ticker": ticker,
            "Shares": shares,
            "Buy_Price": buy_price,
            "Current_Price": curr_price,
            "Total_Invested": round(invested_capital, 2),
            "Current_Value": round(market_val, 2),
            "Gain_Loss_Pct": round(gain_loss_pct, 2)
        })

        print(f"{ticker:<10} | {shares:<8.2f} | ${buy_price:<9.2f} | ${curr_price:<9.2f} | ${invested_capital:<11.2f} | ${market_val:<11.2f} | {gain_loss_pct:>+6.2f}%")

    total_gain_loss_pct = ((total_market_value - total_invested) / total_invested) * 100 if total_invested > 0 else 0

    print("-" * 75)
    print(f"TOTAL INVESTED CAPITAL : ${total_invested:,.2f}")
    print(f"TOTAL PORTFOLIO VALUE  : ${total_market_value:,.2f}")
    print(f"OVERALL PORTFOLIO RETURN: {total_gain_loss_pct:+.2f}%")
    print("="*75)

    # Automatically log summary to external CSV file
    output_file = "portfolio_summary.csv"
    try:
        with open(output_file, mode="w", newline="", encoding="utf-8") as csv_file:
            fieldnames = ["Ticker", "Shares", "Buy_Price", "Current_Price", "Total_Invested", "Current_Value", "Gain_Loss_Pct"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            
            writer.writeheader()
            for row in summary_data:
                writer.writerow(row)
                
        print(f"\n📁 Transaction summary successfully written to '{output_file}'.")
    except Exception as e:
        print(f"⚠️ Failed to write summary CSV: {e}")

if __name__ == "__main__":
    track_portfolio()