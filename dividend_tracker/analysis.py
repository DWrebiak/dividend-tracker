import pandas as pd
from datetime import datetime

def calculate_annual_dividends(dividends: pd.Series) -> dict:
    if dividends is None or dividends.empty:
        return {}

    dividends.index = pd.to_datetime(dividends.index).tz_localize(None)
    annual_sums = dividends.groupby(dividends.index.year).sum().to_dict()

    current_year = datetime.now().year
    if current_year in annual_sums:
        payouts_this_year = dividends[dividends.index.year == current_year]
        if len(payouts_this_year) < 4:
            del annual_sums[current_year]

    return annual_sums

def calculate_cagr(start_value, end_value, years):
    if start_value <= 0 or end_value <= 0 or years <= 0:
        return None
    return (end_value / start_value) ** (1 / years) - 1

def calculate_dividend_cagr(annual_dividends: dict, periods: list[int]) -> dict:
    cagr_results = {}
    sorted_years = sorted(annual_dividends.keys(), reverse=True)

    for period in periods:
        if len(sorted_years) < period + 1:
            cagr_results[f"{period}Y"] = None
            continue

        end_year = sorted_years[0]
        start_year = sorted_years[period]

        start_value = annual_dividends[start_year]
        end_value = annual_dividends[end_year]

        cagr = calculate_cagr(start_value, end_value, period)
        cagr_results[f"{period}Y"] = cagr

    return cagr_results
