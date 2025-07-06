import yfinance as yf

def get_ticker_data(ticker_symbol):
    try:
        ticker = yf.Ticker(ticker_symbol)

        # Fetch basic info
        info = ticker.info or {}
        if not info or "regularMarketPrice" not in info:
            print(f"⚠️ No valid info found for {ticker_symbol}")
            return None, None, None

        # Fetch dividends
        dividends = ticker.dividends
        if dividends.empty:
            dividends = None
        
        # Fetch cashflow
        cashflow = ticker.cashflow
        if cashflow.empty:
            cashflow = None

        return info, dividends, cashflow
    
    except Exception as e:
        print(f"❌ Error fetching data for {ticker_symbol}: {e}")
        return None, None, None
