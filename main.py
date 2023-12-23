import pandas as pd
import os
from datetime import datetime
from helpers.data_processing import DataProcessing
from helpers.html_templates.template_render import TemplateRender
from helpers.logger import Logger
from helpers.validator import Validator
from helpers.trade_analysis import Trade_Analysis

# template_renderer = TemplateRender(template_folder='templates')

## Global Variables 
TIMESTAMP = datetime.now().strftime("%m-%d-%Y_%H:%M:%S")
FILE_PATH = ''
CSV_FILE_NAME = ''
DF = None
HTML_TEMPLATE_DIR = 'templates'


def init_app():
  '''
    This function:
      - Generates a runtime timestamp used for logging and file paths
      - Sets file paths for importing and writing
      - Configures the app wide logging
  '''
  global FILE_PATH
  global CSV_FILE_NAME
  FILE_PATH = input("Enter the relative file path ( I.E. data/raw_data/pairs_test.csv ) : ")
  CSV_FILE_NAME = os.path.splitext(os.path.basename(FILE_PATH))[0]
  Logger.configure_logging(TIMESTAMP, FILE_PATH, CSV_FILE_NAME)


def validate_load_and_clean_data():
  '''
    This function:
      - Validates the file paths and file type
      - Cleans and process the csv
      - Sets the initial Data Frame from cleaned data
  '''
  global DF
  Validator.check_valid_file_path(FILE_PATH)
  Validator.check_file_is_csv(FILE_PATH)
  data_processor = DataProcessing(FILE_PATH)
  DF = data_processor.run_all_data_processing_tasks(TIMESTAMP, CSV_FILE_NAME)


def build_html_template():
  print('building template....')
  template_render = TemplateRender(template_folder=HTML_TEMPLATE_DIR, TIMESTAMP=TIMESTAMP, CSV_FILE_NAME=CSV_FILE_NAME)
  template_render.build_report()


if __name__ == "__main__":
  init_app()
  validate_load_and_clean_data()
  build_html_template()
  print(DF)




# # Import the table component
# table_data = { 'tableTitle': 'MY TABLE TITLE'}
# table_component = template_renderer.render_template('/components/table_component.html', table_data)

# # Define data for the HTML Report template
# data = {
#     'title': 'Analysis Report',
#     'description': 'This is a sample analysis report.',
#     'table_component': table_component,  # Injected table component
# }

# # Render the template
# html_content = template_renderer.render_template('base_template.html', data)
# html_output_filename = f'./data/reports/{timestamp}_{csv_file_name}-report.html'

# # Save the HTML report
# with open(html_output_filename, 'w') as f:
#     f.write(html_content)






# def main():
#     # ...

# def load_and_clean_data(file_path):
#     # ...

# def generate_html_report(df, timestamp, csv_file_name):
#     # ...

# if __name__ == "__main__":
#     main()





# trade_counts_df = Trade_Analysis.calculate_trade_counts(df)
# print(trade_counts_df)
# print('\n')

# mean_number_of_trades = Trade_Analysis.calculate_mean_trades(df)
# print(mean_number_of_trades)
# print('\n')


# trades_ranked_by_count = Trade_Analysis.rank_pairs_by_trade_counts(trade_counts_df)
# print('trades_ranked_by_count')
# print(trades_ranked_by_count)
# print('\n')


# average_duration_by_pair_hours = Trade_Analysis.rank_pairs_by_trade_duration(df)
# print('average_duration_by_pair_hours')
# print(average_duration_by_pair_hours)
# print('\n')


# total_profit_loss_by_pair = Trade_Analysis.rank_pairs_by_total_profit(df)
# print('total_profit_loss_by_pair')
# print(total_profit_loss_by_pair)
# print('\n')

# # Merge the DataFrames on the 'Symbol' column
# combined_df = average_duration_by_pair_hours.merge(total_profit_loss_by_pair, on='Symbol')
# print('Combined DataFrame:')
# print(combined_df)
# print('\n')



# profit_per_hour_of_holding_time = Trade_Analysis.calculate_profit_per_hour_of_holding_time(combined_df)
# print('profit_per_hour_of_holding_time:')
# print(profit_per_hour_of_holding_time)
# print('\n')


# # Merge the DataFrames on the 'Symbol' column
# eval_df = profit_per_hour_of_holding_time.merge(trade_counts_df, on='Symbol')
# print('Eval DataFrame:')
# print(eval_df)
# print('\n')





# average_profit_loss_per_trade_by_pair = df.groupby('Symbol')['Profit'].mean().reset_index()
# print('average_profit_loss_per_trade_by_pair')
# print(average_profit_loss_per_trade_by_pair)
# print('\n')





