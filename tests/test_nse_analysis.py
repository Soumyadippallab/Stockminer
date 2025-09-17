import pytest
from stockminer.nse_analysis import analyze_nse_stocks
import pandas as pd
import numpy as np

def test_analyze_nse_stocks(mocker):
    # Mock dependencies
    mocker.patch('requests.get')
    mocker.patch('yfinance.download')
    mocker.patch('yahooquery.Ticker')
    mocker.patch('time.sleep')
    
    # Run function with limited tickers
    final_summary, _, _, _, _, _ = analyze_nse_stocks(num_tickers=2, top_x=1, start_date="2025-03-18", end_date="2025-09-18")
    
    # Assertions
    assert isinstance(final_summary, pd.DataFrame)
    assert 'Ticker' in final_summary.columns
    assert 'CAGR_%' in final_summary.columns
    assert len(final_summary) <= 2  # Limited by num_tickers