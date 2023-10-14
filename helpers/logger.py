import logging

class Logger:
    
    @staticmethod
    def info(message):
        logging.info(message)
    @staticmethod

    def warn(message):
        logging.warn(message)

    @staticmethod
    def error(message):
        logging.error(message)

    @staticmethod
    def get_log_filename(timestamp, csv_file_name):
        return f'./logs/{timestamp}_{csv_file_name}_log.log'

    @staticmethod
    def configure_logging(timestamp, file_path, csv_file_name):
        log_filename = Logger.get_log_filename(timestamp, csv_file_name)
        logging.basicConfig(filename=log_filename, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        logging.info(f'***** Beginning Parsing For File: {file_path} *****')

    @staticmethod
    def pandas_csv_parse_error(e):
          print(f"ERROR: Could not read CSV: {e}")
          logging.error(f"ERROR: Could not read CSV: {e}")

    @staticmethod
    def method_ran(method_name):
          logging.info(f"Method Ran: {method_name}")

    @staticmethod
    def method_succeeded(method_name):
          logging.info(f"Method Successful: {method_name}")

    @staticmethod
    def method_failed(method_name, e):
          logging.error(f"Method Failed: {method_name} ----- {e}")

    @staticmethod
    def log_dropped_rows(dropped_rows):
        logging.info('The Following Rows Were Dropped:')
        logging.info(dropped_rows)

    @staticmethod
    def csv_cleaned_successfully(df):
        logging.info('***** File Cleaned Successfully *****')
        logging.info('Final DataFrame Output:')
        logging.info(df)

    @staticmethod
    def successfully_saved_new_csv(csv_output_filename):
        logging.info(f'Saved DataFrame as new file: {csv_output_filename}')
        
    @staticmethod
    def failed_to_save_new_csv(e):
        logging.error(f'ERROR: Unable to save a new csv: {e}')
        print(f'ERROR: Unable to save a new csv: {e}')
