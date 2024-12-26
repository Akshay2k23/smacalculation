import pandas as pd

def calculate_sma(input_file, output_file):
    try:
        data = pd.read_csv(input_file)

        columns_to_sma = {
            'Open': 'SMA(Open) 10D',
            'High': 'SMA(High) 10D',
            'Low': 'SMA(Low) 10D',
            'Close': 'SMA(Close) 10D',
            'Adj Close': 'SMA(Adj Close) 10D',
            'Volume': 'SMA(Volume) 10D'
        }

        for col, sma_col in columns_to_sma.items():
            if col in data.columns:
                data[sma_col] = data[col].rolling(window=10).mean()
            else:
                print(f"Column '{col}' is missing in the input file.")

        data.to_csv(output_file, index=False)
        print(f"SMA values calculated and saved to {output_file}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    input_file = "RELIANCE.csv"
    output_file = "RELIANCE_with_SMA.csv"
    calculate_sma(input_file, output_file)

