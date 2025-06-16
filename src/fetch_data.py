# src/fetch_data.py
import yfinance as yf
import os

def download_sp500_data(start="2010-01-01", end="2025-01-01", save_path="data/sp500.csv"):
    print("📈 Downloading S&P 500 data...")
    ticker = "^GSPC"
    df = yf.download(ticker, start=start, end=end, progress=False, auto_adjust=False)

    # Reset index so 'Date' is a column
    df.reset_index(inplace=True)

    # Save only essential columns in clean format
    df = df[['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']]

    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    df.to_csv(save_path, index=False)
    print(f"✅ Data saved to {save_path}")

if __name__ == "__main__":
    download_sp500_data()