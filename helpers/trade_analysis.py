import pandas as pd

class Trade_Analysis():
    @staticmethod
    def calculate_trade_counts(df):
        # Check if 'Symbol' column exists in the DataFrame
        if 'Symbol' not in df.columns:
            raise ValueError("DataFrame does not contain a column named 'Symbol'.")

        # Sum trades for each currency
        trade_counts = df.groupby('Symbol').size().reset_index(name='Trade Count')
        trade_counts = trade_counts.sort_values(by='Trade Count', ascending=False).reset_index(drop=True)

        # Create a new column 'Profitable' indicating whether the trade was profitable or not
        df['Profitable'] = df['Profit'] > 0

        # Calculate the number of profitable and unprofitable trades per currency pair
        profitable_counts = df.groupby(['Symbol', 'Profitable'])['Ticket'].count().unstack(fill_value=0)
        # Rename the columns for clarity
        profitable_counts.columns = ['Loosing Trade Count', 'Profitable Trade Count']
        # Reset the index for a cleaner output
        profitable_counts = profitable_counts.reset_index()
        # Reorder the columns for the desired output
        profitable_counts = profitable_counts[['Symbol', 'Profitable Trade Count', 'Loosing Trade Count']]

        # Combine trade counts and profitability counts into a single DataFrame
        result_df = pd.merge(trade_counts, profitable_counts, on='Symbol', how='left')

        return result_df
    
    @staticmethod
    def calculate_mean_trades(df):
        if 'Symbol' not in df.columns:
            raise ValueError("DataFrame does not contain a column named 'Symbol'.")

        # Group by 'Symbol' and calculate the count of trades
        trade_counts = df.groupby('Symbol')['Ticket'].count().reset_index()
        trade_counts.columns = ['Symbol', 'Trade Count']

        # Calculate the mean trade count
        mean_trade_count = round(trade_counts['Trade Count'].mean(), 2)

        return mean_trade_count




