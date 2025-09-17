import pytest
from stockminer.tda_crash_detection import process_stock_data
import pandas as pd
import numpy as np

def test_process_stock_data(mocker):
    # Mock file loading and dependencies
    mock_data = pd.DataFrame({
        'Date': pd.date_range(start='2025-01-01', periods=100),
        'Close': np.random.rand(100) * 100
    })
    mocker.patch('pandas.read_csv', return_value=mock_data)
    mocker.patch('pandas.read_excel', return_value=mock_data)
    mocker.patch('ripser.ripser')
    mocker.patch('persim.bottleneck')
    mocker.patch('persim.wasserstein')
    
    # Run function with mocked file path
    crash_indices, _, _ = process_stock_data(file_path="dummy.csv")
    
    # Assertions
    assert isinstance(crash_indices, dict)
    assert all(key in crash_indices for key in ['wasserstein', 'bottleneck', 'euclidean', 'manhattan'])
