import yfinance as yf

def get_ticker_data(ticker_symbol):
    ticker = yf.Ticker(ticker_symbol)
    info = ticker.info
    dividends = ticker.dividends
    return info, dividends
