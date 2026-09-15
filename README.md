# Stock Portfolio Tracker 📈

A simple, interactive Python program built for the **CodeAlpha Python Programming Internship (Task 2)**. This application allows users to track their stock investments, calculate total portfolio value based on hardcoded stock market prices, and export detailed reports in `.txt` or `.csv` formats.

---

## 🌟 Features

- **Predefined Stock Market Prices**: Hardcoded dictionary containing popular tickers (`AAPL`, `TSLA`, `GOOGL`, `MSFT`, `AMZN`, `NVDA`, `META`, `NFLX`).
- **Interactive CLI Interface**: User-friendly menu for managing portfolio holdings.
- **Case-Insensitive Ticker Matching**: Accepts ticker symbols in any casing (e.g. `aapl` or `AAPL`).
- **Input Validation**: Ensures valid stock tickers and positive numeric quantities.
- **Total Portfolio Value Calculation**: Automatically computes individual stock values (`quantity * price`) and total investment.
- **Export Options**: Save portfolio reports in **Plain Text (`.txt`)** or **CSV (`.csv`)** format.
- **Unit Test Coverage**: Automated test suite included using Python's built-in `unittest`.

---

## 📂 Project Structure

```text
.
├── portfolio_tracker.py       # Main application script & interactive CLI
├── test_portfolio_tracker.py  # Unit test suite
├── portfolio_summary.txt      # Generated sample plain text report
├── portfolio_summary.csv      # Generated sample CSV report
├── README.md                  # Project documentation
└── .gitignore                 # Standard Python gitignore rules
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher installed on your machine.

### Installation & Running

1. **Clone the Repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/CodeAlpha_Stock_Portfolio_Tracker.git
   cd CodeAlpha_Stock_Portfolio_Tracker
   ```

2. **Run the Application**
   ```bash
   python portfolio_tracker.py
   ```

3. **Run Unit Tests**
   ```bash
   python -m unittest test_portfolio_tracker.py
   ```

---

## 📊 Sample Report Outputs

### Plain Text (`portfolio_summary.txt`)
```text
==================================================
             STOCK PORTFOLIO SUMMARY              
==================================================
Ticker     | Quantity   | Price ($)    | Total ($)   
--------------------------------------------------
AAPL       | 10.00      | $180.00      | $1800.00    
TSLA       | 5.00       | $250.00      | $1250.00    
NVDA       | 15.00      | $120.00      | $1800.00    
--------------------------------------------------
TOTAL PORTFOLIO INVESTMENT VALUE: $4,850.00
==================================================
```

### CSV Output (`portfolio_summary.csv`)
```csv
Ticker,Quantity,Price_USD,Total_Value_USD
AAPL,10.0,180.0,1800.0
TSLA,5.0,250.0,1250.0
NVDA,15.0,120.0,1800.0

TOTAL,,,4850.0
```

---

## 📜 License

This project is open-source and created as part of the CodeAlpha Internship Program.
