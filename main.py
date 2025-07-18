import time
from dividend_tracker.data import get_ticker_data
from dividend_tracker.analysis import calculate_annual_dividends, calculate_dividend_cagr
from dividend_tracker.formatting import format_usd, format_percent
from dividend_tracker.utils import save_dividends_to_csv, load_config

def main():
    # Load config    
    config, config_path, loop_mode = load_config()
    tickers = config.get("tickers", [])
    
    while True:
        all_data = []

        for ticker_symbol in tickers:
            print(f"\n{'='*40}")
            print(f"📊 Analysis for {ticker_symbol}")
            print(f"{'='*40}")

            try:
                info, dividends, cashflow = get_ticker_data(ticker_symbol)    
            except Exception as e:
                print(f"❌ Failed to fetch data for {ticker_symbol}: {e}")
                continue

            if not info or dividends is None or cashflow is None:
                print(f"⚠️ Skipping {ticker_symbol} - no valid data returned.")
                continue

            price = info.get("currentPrice")
            dividend_rate = info.get("dividendRate")
            dividend_yield = info.get("dividendYield")
            payout_ratio = info.get("payoutRatio")        

            fcf = None
            if "Free Cash Flow" in cashflow.index:
                try:                
                    fcf = cashflow.loc["Free Cash Flow"].iloc[0]
                except KeyError as e:
                    print(f"⚠️ Could not calculate FCF for {ticker_symbol}: missing {e}")

            print("=== Dividend Basics ===")
            print("📈 Stock price:", format_usd(price))
            print("💰 Annual dividend:", format_usd(dividend_rate))
            print("📊 Dividend yield:", format_percent(dividend_yield, already_percent=True))
            print("📦 Payout ratio:", format_percent(payout_ratio))
            if fcf is not None:
                print(f"🟢 FCF (Free Cash Flow): {format_usd(fcf, shorten=True)}")
            else:
                print("🟢 FCF (Free Cash Flow): No data")        
            print("")
            print()

            annual_dividends = calculate_annual_dividends(dividends)
            cagr_periods = [1, 3, 5, 10]
            cagr_results = calculate_dividend_cagr(annual_dividends, cagr_periods)

            print("=== Dividend CAGR (annual sums, only full years) ===")
            for period, value in cagr_results.items():
                print(f"📈 {period} CAGR:", format_percent(value))

            record = {
                "Ticker": ticker_symbol,
                "Stock price": format_usd(price),
                "Annual dividend": format_percent(dividend_yield, already_percent=True),
                "Payout ratio": format_percent(payout_ratio),
                "Free Cash Flow": format_usd(fcf, shorten=True),
            }

            for period, value in cagr_results.items():
                record[f"{period} CAGR"] = format_percent(value)

            all_data.append(record)

        save_dividends_to_csv(all_data, config_path)

        if not loop_mode:
            break

        print("⏳ Sleeping for 24 hours before next run...\n")
        time.sleep(86400)

if __name__ == "__main__":
    main()
