from dividend_tracker.data import get_ticker_data
from dividend_tracker.analysis import calculate_annual_dividends, calculate_dividend_cagr
from dividend_tracker.formatting import format_usd, format_percent

def main():
    ticker_symbol = "SWK"
    info, dividends = get_ticker_data(ticker_symbol)

    price = info.get("currentPrice")
    dividend_rate = info.get("dividendRate")
    dividend_yield = info.get("dividendYield")
    payout_ratio = info.get("payoutRatio")

    print("=== Dividend Basics ===")
    print("📈 Stock price:", format_usd(price))
    print("💰 Annual dividend:", format_usd(dividend_rate))
    print("📊 Dividend yield:", format_percent(dividend_yield, already_percent=True))
    print("📦 Payout ratio:", format_percent(payout_ratio))
    print()

    annual_dividends = calculate_annual_dividends(dividends)
    cagr_periods = [1, 3, 5, 10]
    cagr_results = calculate_dividend_cagr(annual_dividends, cagr_periods)

    print("=== Dividend CAGR (annual sums, only full years) ===")
    for label, value in cagr_results.items():
        print(f"📈 {label} CAGR:", format_percent(value))

if __name__ == "__main__":
    main()
