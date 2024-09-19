# import functions
import pandas as pd
import numpy as np
import datetime
import os
import hashlib


# Function to generate synthetic data
def generate_synthetic_data(start_date, end_date, freq="1H"):
    date_rng = pd.date_range(start=start_date, end=end_date, freq=freq)
    data = pd.DataFrame(date_rng, columns=["datetime"])

    # Generate synthetic OHLCV data
    data["open"] = np.random.uniform(low=100, high=200, size=len(date_rng))
    data["high"] = data["open"] + np.random.uniform(low=0, high=10, size=len(date_rng))
    data["low"] = data["open"] - np.random.uniform(low=0, high=10, size=len(date_rng))
    data["close"] = data["open"] + np.random.uniform(low=-5, high=5, size=len(date_rng))
    data["volume"] = np.random.randint(low=100, high=1000, size=len(date_rng))

    # Calculate additional features
    data["SMA_20"] = data["close"].rolling(window=20).mean()
    data["EMA_20"] = data["close"].ewm(span=20, adjust=False).mean()
    data["returns"] = data["close"].pct_change()
    data["volatility"] = data["returns"].rolling(window=20).std()
    data["RSI"] = compute_rsi(data["close"], window=14)
    data["MACD"] = (
        data["close"].ewm(span=12, adjust=False).mean()
        - data["close"].ewm(span=26, adjust=False).mean()
    )
    data["Signal_Line"] = data["MACD"].ewm(span=9, adjust=False).mean()

    # Drop rows with NaN values
    data.dropna(inplace=True)

    return data


def compute_rsi(data, window):
    delta = data.diff(1)
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
    rs = gain / loss
    return 100 - (100 / (1 + rs))


# Generate synthetic data from 2023-01-01 to 2023-12-31 with hourly frequency
synthetic_data = generate_synthetic_data("2023-01-01", "2023-12-31", freq="1H")

# Verify current directory and save the file
current_directory = os.getcwd()
print(f"Current Directory: {current_directory}")

file_path = os.path.join(current_directory, "synthetic_market_trends_data.csv")
synthetic_data.to_csv(file_path, index=False)

print(f"Data saved to {file_path}")
print(synthetic_data.head())
