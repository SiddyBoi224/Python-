import yfinance as yf
import time

# List of Indian stock symbols (replace with your specific stock symbols)
# Append ".NS" for stocks listed on NSE
stocks = ["RELIANCE.NS", "TCS.NS", "HDFCBANK.NS"]

def fetch_stock_data():
    for stock in stocks:
        try:
            # Fetch stock data
            ticker = yf.Ticker(stock)
            stock_info = ticker.history(period="1d", interval="1m")
            # Get the latest stock price
            latest_price = stock_info['Close'].iloc[-1]
            print(f"{stock}: ₹{latest_price}")
        except Exception as e:
            print(f"Error fetching data for {stock}: {e}")

if __name__ == "__main__":
    # Infinite loop to constantly check stock data
    print("Starting to fetch stock data...\n")
    while True:
        fetch_stock_data()
        print("\nWaiting for next update...\n")
        # Delay for 60 seconds before the next fetch
        time.sleep(30)

#Use Ctrl + C to stop the infinite

