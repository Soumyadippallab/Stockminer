import sys
import argparse

def display_help():
    """Display help message summarizing available functions and their inputs."""
    help_text = """
StockMiner: A Python package for NSE stock and market index analysis.

Usage: python -m stockminer [options]

Options:
  -h, --help    Show this help message and exit

Available Functions:
1. analyze_nse_stocks(num_tickers=None, top_x=None, start_date=None, end_date=None)
   - Analyzes NSE stocks with company-wise and sector-wise metrics (returns, volatility, CAGR, etc.).
   - Inputs:
     - num_tickers: Integer (optional, default None for all NSE stocks) - Limit number of stocks.
     - top_x: Integer (optional, default 5) - Number of top companies to display by CAGR.
     - start_date: YYYY-MM-DD (optional, default 6 months prior, e.g., 2025-03-18) - Analysis start date.
     - end_date: YYYY-MM-DD (optional, default today, e.g., 2025-09-18) - Analysis end date.

2. analyze_market_indices(start_date=None, end_date=None)
   - Analyzes SENSEX and NIFTY indices with user-defined highlight periods.
   - Inputs:
     - start_date: YYYY-MM-DD (optional, default 6 months prior, e.g., 2025-03-18) - Analysis start date.
     - end_date: YYYY-MM-DD (optional, default today, e.g., 2025-09-18) - Analysis end date.
     - Prompts for number of highlight periods, their names, and start/end dates (default none).

3. process_stock_data(file_path=None, dimension=3, delay=1, window_size=50, homology_dims=[0, 1], bottleneck_threshold=0.01, other_threshold=0.05, price_drop_threshold=-7)
   - Detects market crashes in stock data using topological data analysis (TDA).
   - Inputs:
     - file_path: String (required, prompts if None) - Path to CSV/XLSX file with 'Date' and 'Close' columns.
     - Other parameters are fixed (no user input):
       - dimension: Embedding dimension (default 3).
       - delay: Embedding delay (default 1).
       - window_size: Sliding window size (default 50).
       - homology_dims: Homology dimensions (default [0, 1]).
       - bottleneck_threshold: Bottleneck distance threshold (default 0.01).
       - other_threshold: Threshold for other distances (default 0.05).
       - price_drop_threshold: Price drop percentage for crash (default -7).

4. analyze_random_stocks_or_sectors(k=None, selection_type="companies", start_date=None, end_date=None)
   - Analyzes k randomly selected companies or sectors with statistical metrics.
   - Inputs:
     - k: Integer (optional, default 5) - Number of random selections.
     - selection_type: String (optional, default "companies") - "companies" or "sectors".
     - start_date: YYYY-MM-DD (optional, default 6 months prior, e.g., 2025-03-18) - Analysis start date.
     - end_date: YYYY-MM-DD (optional, default today, e.g., 2025-09-18) - Analysis end date.

To run a function, import it in Python:
    from stockminer import analyze_nse_stocks
    results = analyze_nse_stocks()

For more details, see README.md.
"""
    print(help_text)

def main():
    """Main entry point for the stockminer CLI."""
    parser = argparse.ArgumentParser(description="StockMiner CLI", add_help=False)
    parser.add_argument('-h', '--help', action='store_true', help="Show help message and exit")
    args = parser.parse_args()
    
    if args.help:
        display_help()
        sys.exit(0)
    
    # If no arguments provided, show help
    display_help()
    sys.exit(0)

if __name__ == "__main__":
    main()
