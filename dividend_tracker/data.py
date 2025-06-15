import yfinance as yf

def get_ticker_data(ticker_symbol):
    try:
        ticker = yf.Ticker(ticker_symbol)
        info = ticker.info or {}
        dividends = ticker.dividends if not ticker.dividends.empty else None
        cashflow = ticker.cashflow if not ticker.cashflow.empty else None
        return info, dividends, cashflow
    except Exception as e:
        print(f"❌ Error fetching data for {ticker_symbol}: {e}")
        return {}, None, None
