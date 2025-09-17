import pytest
from stockminer.market_index_analysis import analyze_market_indices
import pandas as pd

def test_analyze_market_indices(mocker):
    # Mock dependencies
    mocker.patch('yfinance.download')
    
    # Run function with fixed dates
    df, _, _ = analyze_market_indices(start_date="2025-03-18", end_date="2025-09-18")
    
    # Assertions
    assert isinstance(df, pd.DataFrame)
    assert 'Period' in df.columns
    assert len(df) >= 1  # At least the overall period
