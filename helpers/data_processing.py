import pandas as pd
from datetime import datetime
from helpers.logger import Logger



class DataProcessing():
    FILE_PATH = None

    def __init__(self, FILE_PATH):
        self.FILE_PATH = FILE_PATH

    def run_all_data_processing_tasks(self, TIMESTAMP, csv_file_name):
        df  = self.load_csv_to_df(self.FILE_PATH)
        df  = self.remove_blank_rows(df)
        df  = self.remove_open_trade_rows(df)
        df = self.remove_deposit_rows(df)
        df = self.remove_withdrawal_rows(df)
        df = self.calculate_trade_durations(df)
        df = self.remove_tags_column(df)
        df = df.reset_index(drop=True)
        Logger.csv_cleaned_successfully(df)
        self.save_df_as_csv(df, TIMESTAMP, csv_file_name)
        return df 


    @staticmethod
    def load_csv_to_df(file_path):
        try:
            df = pd.read_csv(file_path)
            if df.empty:
                message = "Loaded DataFrame is empty."
                print(message)
                Logger.error(message)
                raise ValueError(message)
            return df
        except pd.errors.ParserError as e:
            Logger.pandas_csv_parse_error(e)
            exit()


    @staticmethod
    def get_log_filename(timestamp, csv_file_name):
        return f"./logs/{timestamp}_{csv_file_name}-log.log"


    @staticmethod
    def remove_blank_rows(df):
        Logger.method_ran('remove_blank_rows')
        try:
            df = df.dropna(how='all').reset_index(drop=True)
            Logger.method_succeeded('remove_blank_rows')
        except Exception as e:
            Logger.method_failed('remove_blank_rows', e)
        return df


    @staticmethod
    def remove_open_trade_rows(df):
        Logger.method_ran('remove_open_trade_rows')
        try:
            # Check if any column contains the value "Open Trades"
            open_trades_mask = df.eq('Open Trades').any(axis=1)
            # Find the index where the value is "Open Trades"
            open_trades_index = open_trades_mask[open_trades_mask].index
            # If there are rows with "Open Trades"
            if not open_trades_index.empty:
                # Get the index of the first occurrence
                first_open_trades_index = open_trades_index[0]
                # Save the rows that will be dropped
                dropped_rows = df.loc[first_open_trades_index:]
                # Drop rows starting from the first occurrence of "Open Trades" onwards
                df = df.loc[:first_open_trades_index - 1]
                Logger.method_succeeded('remove_open_trade_rows')
                Logger.log_dropped_rows(dropped_rows)
            else:
                dropped_rows = None
                Logger.warn("No rows found with Open Trades. Skipping drop operation.")
        except Exception as e:
            Logger.method_failed('remove_open_trade_rows', e)
        return df


    @staticmethod
    def remove_deposit_rows(df):
        Logger.method_ran('remove_deposit_rows')
        try:
            dropped_rows = df[df['Action'].isin(['Deposit'])]
            if dropped_rows.empty:
                Logger.warn("No rows found with Action 'Deposit'. Skipping drop operation.")
            else:
                Logger.method_succeeded('remove_deposit_rows')
                Logger.log_dropped_rows(dropped_rows)
                df = df[~df['Action'].isin(['Deposit'])]
        except Exception as e:
            Logger.method_failed('remove_deposit_rows', e)
        return df


    @staticmethod
    def remove_withdrawal_rows(df):
        Logger.method_ran('remove_withdrawal_rows')
        try:
            dropped_rows = df[df['Action'].isin(['Withdrawal'])]
            if dropped_rows.empty:
                Logger.warn("No rows found with action 'Withdrawal'. Skipping drop operation.")
            else:
                Logger.method_succeeded('remove_withdrawal_rows')
                Logger.log_dropped_rows(dropped_rows)
                df = df[~df['Action'].isin(['Withdrawal'])]
        except Exception as e:
            Logger.method_failed('remove_withdrawal_rows', e)
        return df


    @staticmethod
    def custom_to_timedelta(duration_str):
        days, hh, mm, ss = map(int, duration_str.split(':'))
        return pd.Timedelta(days=days, hours=hh, minutes=mm, seconds=ss)


    @staticmethod
    def calculate_trade_durations(df):
        Logger.method_ran('calculate_trade_durations')
        try:
            # Apply the function to the column and create a new timedelta column
            df['Duration'] = df['Duration (DD:HH:MM:SS)'].apply(DataProcessing.custom_to_timedelta)
            Logger.info("Converted strings in column 'Duration (DD:HH:MM:SS)' to datetimes in column 'Duration' ")
            # Delete the column 'Duration (DD:HH:MM:SS)'
            if 'Duration (DD:HH:MM:SS)' in df.columns:
                df = df.drop(columns=['Duration (DD:HH:MM:SS)'])
                Logger.method_succeeded('calculate_trade_durations')
                Logger.info("Dropped Column 'Duration (DD:HH:MM:SS)' ")
            else:
                Logger.warning("Column 'Duration (DD:HH:MM:SS)' not found. Skipping drop operation.")
            return df
        except Exception as e:
            Logger.method_failed('calculate_trade_durations', e)
            return df


    @staticmethod
    def remove_tags_column(df):
        Logger.method_ran('remove_tags_column')
        try:
            Logger.method_succeeded('remove_tags_column')
            Logger.info("Dropped Column 'Tags' ")
            return df.drop(columns=['Tags'])
        except KeyError as e:
            Logger.warning("Column 'Tags' not found. Skipping drop operation.")
            return df  
        except Exception as e:
            Logger.method_failed('remove_tags_column', e)
            return df  


    @staticmethod
    def save_df_as_csv(df, timestamp, csv_file_name):
        try:
            # Save the cleaned DataFrame as a new CSV file
            csv_output_filename = f'./data/clean_data/{timestamp}_{csv_file_name}-cleaned.csv'
            df.to_csv(csv_output_filename, index=False)
            Logger.successfully_saved_new_csv(csv_output_filename)
        except Exception as e:
            Logger.failed_to_save_new_csv(e)
    

