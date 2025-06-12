from dividend_tracker.data import get_ticker_data
from dividend_tracker.analysis import calculate_annual_dividends, calculate_dividend_cagr
from dividend_tracker.formatting import format_usd, format_percent
from dividend_tracker.utils import save_dividends_to_csv

def main():
    #tickers = ["AOS", "ABBV", "ALB", "BDX", "CSL", "CAT", "CL", "DOV", "ED", "EMR",
    #"ITW", "JNJ", "LOW", "MDT", "NEE", "PEP", "O", "ROP", "SWK", "TGT", "KO"]
    tickers = ["AOS", "ABBV"]
    all_data = []

    for ticker_symbol in tickers:
        print(f"\n{'='*40}")
        print(f"📊 Analysis for {ticker_symbol}")
        print(f"{'='*40}")
    
        info, dividends, cashflow = get_ticker_data(ticker_symbol)

        #print("Available cashflow rows:", cashflow.index.tolist())

        price = info.get("currentPrice")
        dividend_rate = info.get("dividendRate")
        dividend_yield = info.get("dividendYield")
        payout_ratio = info.get("payoutRatio")
        #fcf = cashflow.loc["Total Cash From Operating Activities"] - cashflow.loc["Capital Expenditures"]

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
            print(f"🟢 FCF (Free Cash Flow): {format_usd(fcf)}")
        else:
            print("🟢 FCF (Free Cash Flow): No data")
        #print("🟢 FCF (Free Cash Flow):", fcf[0])
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
        }

        for period, value in cagr_results.items():
            record[f"{period} CAGR"] = format_percent(value)

        

        all_data.append(record)

    save_dividends_to_csv(all_data, "dividend_data.csv")

if __name__ == "__main__":
    main()
