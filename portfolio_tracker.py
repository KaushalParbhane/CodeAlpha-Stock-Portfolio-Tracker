"""
Task 2: Stock Portfolio Tracker
CodeAlpha Python Programming Internship

Calculates total investment value based on defined stock prices,
allows user input for stock names and quantities, and saves reports in .txt or .csv format.
"""

import csv
import os
from typing import Dict, Tuple

# Hardcoded stock price dictionary
DEFAULT_STOCK_PRICES: Dict[str, float] = {
    "AAPL": 180.0,
    "TSLA": 250.0,
    "GOOGL": 140.0,
    "MSFT": 400.0,
    "AMZN": 175.0,
    "NVDA": 120.0,
    "META": 480.0,
    "NFLX": 600.0,
}


class StockPortfolioTracker:
    def __init__(self, stock_prices: Dict[str, float] = None):
        """Initialize tracker with stock prices dictionary and empty portfolio."""
        if stock_prices is None:
            self.stock_prices = DEFAULT_STOCK_PRICES.copy()
        else:
            self.stock_prices = {k.upper(): float(v) for k, v in stock_prices.items()}
        
        # Portfolio dictionary mapping uppercase ticker to quantity
        self.portfolio: Dict[str, float] = {}

    def is_valid_stock(self, ticker: str) -> bool:
        """Check if stock ticker exists in the price dictionary."""
        return ticker.upper() in self.stock_prices

    def get_price(self, ticker: str) -> float:
        """Get the price of a stock ticker."""
        return self.stock_prices.get(ticker.upper(), 0.0)

    def add_stock(self, ticker: str, quantity: float) -> Tuple[bool, str]:
        """Add or update stock quantity in the portfolio."""
        ticker = ticker.upper().strip()
        if not ticker:
            return False, "Stock ticker cannot be empty."

        if not self.is_valid_stock(ticker):
            return False, f"Stock '{ticker}' is not available in stock price list."

        if quantity <= 0:
            return False, "Quantity must be greater than zero."

        current_qty = self.portfolio.get(ticker, 0.0)
        self.portfolio[ticker] = current_qty + quantity
        return True, f"Successfully added {quantity} share(s) of {ticker}."

    def remove_stock(self, ticker: str) -> Tuple[bool, str]:
        """Remove stock from portfolio."""
        ticker = ticker.upper().strip()
        if ticker in self.portfolio:
            del self.portfolio[ticker]
            return True, f"Removed {ticker} from portfolio."
        return False, f"Stock '{ticker}' is not in your portfolio."

    def calculate_item_value(self, ticker: str) -> float:
        """Calculate total value for a single stock holding."""
        ticker = ticker.upper()
        quantity = self.portfolio.get(ticker, 0.0)
        price = self.get_price(ticker)
        return quantity * price

    def calculate_total_investment(self) -> float:
        """Calculate total investment value of the entire portfolio."""
        total = 0.0
        for ticker in self.portfolio:
            total += self.calculate_item_value(ticker)
        return total

    def save_to_txt(self, filepath: str = "portfolio_summary.txt") -> str:
        """Export portfolio summary to a plain text file."""
        lines = []
        lines.append("==================================================")
        lines.append("             STOCK PORTFOLIO SUMMARY              ")
        lines.append("==================================================")
        lines.append(f"{'Ticker':<10} | {'Quantity':<10} | {'Price ($)':<12} | {'Total ($)':<12}")
        lines.append("-" * 50)

        total_value = 0.0
        for ticker, qty in self.portfolio.items():
            price = self.get_price(ticker)
            item_val = qty * price
            total_value += item_val
            lines.append(f"{ticker:<10} | {qty:<10.2f} | ${price:<11.2f} | ${item_val:<11.2f}")

        lines.append("-" * 50)
        lines.append(f"TOTAL PORTFOLIO INVESTMENT VALUE: ${total_value:,.2f}")
        lines.append("==================================================")

        with open(filepath, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))

        return os.path.abspath(filepath)

    def save_to_csv(self, filepath: str = "portfolio_summary.csv") -> str:
        """Export portfolio summary to a CSV file."""
        with open(filepath, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Ticker", "Quantity", "Price_USD", "Total_Value_USD"])
            
            total_value = 0.0
            for ticker, qty in self.portfolio.items():
                price = self.get_price(ticker)
                item_val = qty * price
                total_value += item_val
                writer.writerow([ticker, round(qty, 2), round(price, 2), round(item_val, 2)])
            
            writer.writerow([])
            writer.writerow(["TOTAL", "", "", round(total_value, 2)])

        return os.path.abspath(filepath)


def display_menu():
    """Print CLI interface menu."""
    print("\n" + "=" * 45)
    print("        STOCK PORTFOLIO TRACKER MENU         ")
    print("=" * 45)
    print("1. View Market Stock Prices")
    print("2. Add Stock to Portfolio")
    print("3. Remove Stock from Portfolio")
    print("4. View Portfolio Summary & Total Investment")
    print("5. Save Portfolio Report (.txt / .csv)")
    print("6. Exit")
    print("=" * 45)


def main():
    tracker = StockPortfolioTracker()
    print("Welcome to Stock Portfolio Tracker!")

    while True:
        display_menu()
        choice = input("Select an option (1-6): ").strip()

        if choice == "1":
            print("\nAvailable Stock Market Prices:")
            print(f"{'Ticker':<10} | {'Price ($)':<10}")
            print("-" * 25)
            for ticker, price in tracker.stock_prices.items():
                print(f"{ticker:<10} | ${price:<10.2f}")

        elif choice == "2":
            ticker = input("\nEnter Stock Ticker (e.g. AAPL, TSLA): ").strip().upper()
            if not tracker.is_valid_stock(ticker):
                print(f"Error: '{ticker}' is not in the price list. Available: {', '.join(tracker.stock_prices.keys())}")
                continue
            
            try:
                quantity_str = input(f"Enter quantity of {ticker}: ").strip()
                quantity = float(quantity_str)
                success, msg = tracker.add_stock(ticker, quantity)
                print(f"\n{msg}")
            except ValueError:
                print("Error: Invalid quantity. Please enter a numerical value.")

        elif choice == "3":
            if not tracker.portfolio:
                print("\nYour portfolio is currently empty.")
                continue

            ticker = input("\nEnter Stock Ticker to remove: ").strip().upper()
            success, msg = tracker.remove_stock(ticker)
            print(f"\n{msg}")

        elif choice == "4":
            if not tracker.portfolio:
                print("\nYour portfolio is currently empty.")
            else:
                print("\n" + "-" * 52)
                print("                 PORTFOLIO SUMMARY                ")
                print("-" * 52)
                print(f"{'Ticker':<10} | {'Quantity':<10} | {'Price ($)':<12} | {'Total ($)':<12}")
                print("-" * 52)
                for ticker, qty in tracker.portfolio.items():
                    price = tracker.get_price(ticker)
                    item_val = tracker.calculate_item_value(ticker)
                    print(f"{ticker:<10} | {qty:<10.2f} | ${price:<11.2f} | ${item_val:<11.2f}")
                print("-" * 52)
                total = tracker.calculate_total_investment()
                print(f"TOTAL INVESTMENT VALUE: ${total:,.2f}")
                print("-" * 52)

        elif choice == "5":
            if not tracker.portfolio:
                print("\nYour portfolio is empty. Add stocks before saving a report.")
                continue

            print("\nSelect Export Format:")
            print("1. Text File (.txt)")
            print("2. CSV File (.csv)")
            print("3. Both (.txt and .csv)")
            fmt_choice = input("Enter choice (1-3): ").strip()

            if fmt_choice == "1":
                path = tracker.save_to_txt()
                print(f"\nSaved report to: {path}")
            elif fmt_choice == "2":
                path = tracker.save_to_csv()
                print(f"\nSaved report to: {path}")
            elif fmt_choice == "3":
                txt_path = tracker.save_to_txt()
                csv_path = tracker.save_to_csv()
                print(f"\nSaved text report to: {txt_path}")
                print(f"Saved CSV report to: {csv_path}")
            else:
                print("Invalid export option.")

        elif choice == "6":
            print("\nThank you for using Stock Portfolio Tracker. Goodbye!")
            break

        else:
            print("\nInvalid choice. Please select a number from 1 to 6.")


if __name__ == "__main__":
    main()
