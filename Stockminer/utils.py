from datetime import datetime
from dateutil.relativedelta import relativedelta
import pandas as pd
import numpy as np

def get_date_input(prompt, default_date):
    """Prompt for a date input, return default if empty."""
    date_str = input(f"{prompt} (YYYY-MM-DD, press Enter for {default_date.strftime('%Y-%m-%d')}): ").strip()
    if not date_str:
        return default_date
    try:
        return pd.to_datetime(date_str)
    except ValueError:
        print(f"Invalid date format. Using default: {default_date.strftime('%Y-%m-%d')}")
        return default_date

def get_default_dates():
    """Return default start (6 months prior) and end (current month end) dates."""
    current_date = datetime.now()
    end_date = current_date.replace(day=1) + relativedelta(months=1) - relativedelta(days=1)
    start_date = current_date - relativedelta(months=6)
    start_date = start_date.replace(day=1)
    return start_date, end_date

def get_integer_input(prompt, default=5):
    """Prompt for an integer input, return default of 5 if empty."""
    response = input(f"{prompt} (press Enter for {default}): ").strip()
    if not response:
        return default
    try:
        return int(response)
    except ValueError:
        print(f"Invalid input. Using default: {default}")
        return default

def calculate_cagr(start_price, end_price, days):
    """Calculate Compound Annual Growth Rate (CAGR)."""
    if days <= 0 or start_price <= 0 or end_price <= 0:
        return np.nan
    years = days / 365.0
    return (end_price / start_price) ** (1 / years) - 1

def validate_file_path(file_path):
    """Validate if file exists and is CSV/XLSX."""
    import os
    file_path = file_path.strip().strip("'").strip('"')
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    if not (file_path.lower().endswith('.csv') or file_path.lower().endswith('.xlsx')):
        raise ValueError("File must be .csv or .xlsx")
    return file_path
