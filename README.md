# StockMiner

StockMiner is a Python package for analyzing NSE (National Stock Exchange of India) stocks and market indices (SENSEX and NIFTY), performing topological data analysis (TDA) for crash detection, and analyzing randomly selected companies or sectors. It provides comprehensive statistical metrics and visualizations for financial data analysis.

## Features

- **NSE Stock Analysis**: Analyzes NSE stocks with company-wise and sector-wise metrics (returns, volatility, trend slopes, Sharpe ratios, CAGR).
- **Market Index Analysis**: Analyzes SENSEX and NIFTY indices with user-defined highlight periods, computing trends, returns, volatility, and correlations.
- **TDA Crash Detection**: Detects market crashes in stock data using topological data analysis with persistence diagrams and distance metrics.
- **Random Selection Analysis**: Analyzes a random subset of companies or sectors with statistical metrics and visualizations.

## Installation

1. Clone the repository or install via pip (once published to PyPI):
   ```bash
   pip install stockminer


Install dependencies:pip install -r requirements.txt


Ensure Python 3.8 or higher is installed.

Usage
NSE Stock Analysis
from stockminer import analyze_nse_stocks

# Analyze up to 10 stocks, show top 5 by CAGR
results = analyze_nse_stocks(num_tickers=10, top_x=5)

Market Index Analysis
from stockminer import analyze_market_indices

# Analyze indices with custom highlight periods
results = analyze_market_indices()

TDA Crash Detection
from stockminer import process_stock_data

# Analyze stock data from a CSV file
crash_indices, timestamps, prices = process_stock_data(file_path="stock_data.csv")

Random Selection Analysis
from stockminer import analyze_random_stocks_or_sectors

# Analyze 5 random companies
results = analyze_random_stocks_or_sectors(k=5, selection_type="companies")

Requirements
See requirements.txt for a full list of dependencies, including:

pandas>=2.0.0
yfinance>=0.2.40
yahooquery>=2.3.0
numpy>=1.26.0
scikit-learn>=1.4.2
scipy>=1.13.1
matplotlib>=3.9.0
seaborn>=0.13.2
ripser>=0.6.4
persim>=0.3.5
openpyxl>=3.1.2

Running Tests
Unit tests are provided in the tests/ directory. Run them using pytest:
pytest tests/

License
This project is licensed under the MIT License.```