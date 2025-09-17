import pytest
from stockminer.random_selection_analysis import analyze_random_stocks_or_sectors
import pandas as pd

def test_analyze_random_stocks_or_sectors(mocker):
    # Mock dependencies
    mocker.patch('requests.get')
    mocker.patch('yfinance.download')
    mocker.patch('yahooquery.Ticker')
    mocker.patch('time.sleep')
    
    # Run function with limited selection
    final_summary, _, _, _ = analyze_random_stocks_or_sectors(k=2, selection_type="companies", start_date="2025-03-18", end_date="2025-09-18")
    
    # Assertions
    assert isinstance(final_summary, pd.DataFrame)
    assert 'Ticker' in final_summary.columns
    assert 'CAGR_%' in final_summary.columns
    assert 'Sector' in final_summary.columns
    assert len(final_summary) <= 2  # Limited by k
