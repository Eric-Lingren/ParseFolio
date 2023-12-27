import pandas as pd

class Trade_Analysis():
    @staticmethod
    def calculate_trade_counts_by_symbol(df):
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
    
    @staticmethod
    def rank_pairs_by_trade_counts(df):
        # # Calculate the rank for each pair based on profitable trade count
        no_losing_trades = df[df['Loosing Trade Count'] == 0]

        # Sort the filtered DataFrame by profitable trade count in descending order
        sorted_no_losing_trades = no_losing_trades.sort_values(by='Profitable Trade Count', ascending=False)

        # Get the indices of the sorted rows
        sorted_indices = sorted_no_losing_trades.index

        # Create a mask to identify the remaining rows with losing trade counts
        remaining_mask = ~df.index.isin(sorted_indices)

        # Get the remaining rows
        remaining_rows = df[remaining_mask]

        # Concatenate the sorted portion with the remaining data
        ranked_df = pd.concat([sorted_no_losing_trades, remaining_rows])

        # Reset the index for cleaner output
        ranked_df = ranked_df.reset_index(drop=True)

        # Return the ranked pairs in the same format as the input
        return ranked_df[['Symbol', 'Trade Count', 'Profitable Trade Count', 'Loosing Trade Count']]



    @staticmethod
    def rank_pairs_by_trade_duration(df):
        # Convert 'Duration' to total seconds (numeric value)
        df['Duration'] = df['Duration'].dt.total_seconds()
        # # Group by 'Symbol' and calculate the average duration in seconds
        average_duration_by_pair_hours = df.groupby('Symbol')['Duration'].mean().reset_index()
        # Convert average duration to hours
        average_duration_by_pair_hours['Duration'] = average_duration_by_pair_hours['Duration'] / 60
        # Convert average duration to hours
        average_duration_by_pair_hours['Duration'] = average_duration_by_pair_hours['Duration'] / 60
        # return average_duration_by_pair_hours
        # Sort the DataFrame by duration in ascending order (shortest duration first)
        sorted_df = average_duration_by_pair_hours.sort_values(by='Duration', ascending=True)
        # Reset the index for cleaner output
        sorted_df = sorted_df.reset_index(drop=True)
        
        return sorted_df

    @staticmethod
    def rank_pairs_by_total_profit(df):
        total_profit_loss_by_pair = df.groupby('Symbol')['Profit'].sum()
        sorted_df = total_profit_loss_by_pair.sort_values(ascending=False).reset_index()
        return sorted_df
    

    @staticmethod
    def calculate_profit_per_hour_of_holding_time(df):
        # Calculate average profit per hour
        df['Average Profit per Hour'] = df['Profit'] / df['Duration']\

        # Sort the DataFrame by 'Average Profit per Hour' in descending order
        sorted_df = df.sort_values(by='Average Profit per Hour', ascending=False)

        # Reset the index for cleaner output
        sorted_df = sorted_df.reset_index(drop=True)

        return sorted_df




