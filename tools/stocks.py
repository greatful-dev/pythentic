from datetime import datetime
import yfinance as yf
import pandas as pd

def pentagon_momentum_scores(ticker):
    try:
        stock = yf.Ticker(ticker)
        info = stock.info

        # 1. PEG Ratio < 2
        peg = info.get('trailingPegRatio', 99) < 2

        # 2. Debt to Equity < 40% (0.4)
        de = info.get('debtToEquity', 999) < 40

        # 3. ROE > 15%
        roe = info.get('returnOnEquity', 0) > 0.15

        # 4. RSI > 50 (Requires historical data)
        hist = stock.history(period="1mo")
        delta = hist['Close'].diff()
        gain = (delta.where(delta > 0, 0)).mean()
        loss = (-delta.where(delta < 0, 0)).mean()
        rs = gain / loss
        rsi = True if 100 - (100 / (1 + rs)) > 50 else False

        # 5. Earnings Quality (Cash Flow / Net Income > 1.0)
        # A simple proxy: Operating Cash Flow should ideally exceed Net Income
        ocf = info.get('operatingCashflow', 0)
        ni = info.get('netIncomeToCommon', 1)
        quality = (ocf / ni) > 1.0

        return {
            'ticker': ticker,
            'passed': all([ticker, peg, de, roe, rsi, quality]),
            'pegRatio': info.get('trailingPegRatio', 99),
            'debt_to_equity': info.get('debtToEquity', 999),
            'return_on_equity': info.get('returnOnEquity', 0),
            'relative_strength_indicator':  100 - (100 / (1 + rs)),
            'operating_cashflow_over_net_income': (ocf / ni)
        }

    except Exception as e:
        return

def get_spy_holdings():
    url = 'https://www.ssga.com/us/en/intermediary/etfs/library-content/products/fund-data/etfs/us/holdings-daily-us-en-spy.xlsx'
    # Read the Excel file, skipping the initial rows
    df = pd.read_excel(url, skiprows=4)

    # The 'Ticker' column contains the symbols
    tickers = df['Ticker'].dropna().to_list()

    return tickers
