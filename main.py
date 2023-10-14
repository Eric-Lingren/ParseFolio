import pandas as pd
import os
import logging
from datetime import datetime
from helpers.data_processing import DataProcessing
from helpers.template_renderer import TemplateRenderer
from helpers.logger import Logger
from helpers.validator import Validator
from helpers.trade_analysis import Trade_Analysis


timestamp = DataProcessing.get_current_timestamp()
template_renderer = TemplateRenderer(template_folder='templates')

file_path = input("Enter the relative file path ( I.E. data/raw_data/pairs_test.csv ) : ")
csv_file_name = os.path.splitext(os.path.basename(file_path))[0]

Logger.configure_logging(timestamp, file_path, csv_file_name)

Validator.check_valid_file_path(file_path)
Validator.check_file_is_csv(file_path)

df = DataProcessing.load_csv_to_df(file_path)
df = DataProcessing.remove_blank_rows(df)
df = DataProcessing.remove_open_trade_rows(df)
df = DataProcessing.remove_deposit_rows(df)
df = DataProcessing.remove_withdrawal_rows(df)
df = DataProcessing.calculate_trade_durations(df)
df = DataProcessing.remove_tags_column(df)
df = df.reset_index(drop=True)
Logger.csv_cleaned_successfully(df)
# DataProcessing.save_df_as_csv(df, timestamp, csv_file_name)


# Define data for the HTML Report template
# data = {
#     'title': 'Analysis Report',
#     'description': 'This is a sample analysis report.',
#     'dataframe': df.to_html(classes='dataframe table table-bordered', index=False),  # Convert DataFrame to HTML
#     # Add chart data and rendering here if needed
# }

# # Render the template
# html_content = template_renderer.render_template('base_template.html', data)
# html_output_filename = f'./data/reports/{timestamp}_{csv_file_name}-report.html'

# # Save the HTML report
# with open(html_output_filename, 'w') as f:
#     f.write(html_content)

# logging.info(f'Saved Report as : {html_output_filename}')



print('\n\n\n\n')
print(df)
print('\n\n\n\n')
column_headers = df.columns
# Print the column headers
print(column_headers)


trade_counts_df = Trade_Analysis.calculate_trade_counts(df)
print(trade_counts_df)
print('\n')

mean_number_of_trades = Trade_Analysis.calculate_mean_trades(df)
print(mean_number_of_trades)
print('\n')


# Convert 'Duration' to total seconds (numeric value)
df['Duration'] = df['Duration'].dt.total_seconds()
# # Group by 'Symbol' and calculate the average duration in seconds
average_duration_by_pair_hours = df.groupby('Symbol')['Duration'].mean().reset_index()
# Convert average duration to hours
average_duration_by_pair_hours['Duration'] = average_duration_by_pair_hours['Duration'] / 60
# Convert average duration to hours
average_duration_by_pair_hours['Duration'] = average_duration_by_pair_hours['Duration'] / 60
print('average_duration_by_pair_hours')
print(average_duration_by_pair_hours)
print('\n')

# Assuming 'Profit' column contains the profit or loss values
total_profit_loss_by_pair = df.groupby('Symbol')['Profit'].sum().reset_index()
print('total_profit_loss_by_pair')
print(total_profit_loss_by_pair)
print('\n')

# Assuming 'Profit' column contains the profit or loss values
average_profit_loss_per_trade_by_pair = df.groupby('Symbol')['Profit'].mean().reset_index()
print('average_profit_loss_per_trade_by_pair')
print(average_profit_loss_per_trade_by_pair)
print('\n')





