import plotly.express as px
from helpers.trade_analysis import Trade_Analysis


class Chart():
    @staticmethod
    def generate_trade_counts_by_symbol(df):
        trade_counts_df = Trade_Analysis.calculate_trade_counts_by_symbol(df)

        fig = px.bar(trade_counts_df, x='Symbol', y=['Profitable Trade Count', 'Loosing Trade Count'],
                    title='Trade Counts by Symbol',
                    labels={'value': 'Count', 'variable': 'Trade Type'})

        chart_html = fig.to_html(full_html=False)
        return chart_html
    

    def generate_average_trade_duration_by_symbol(df):
      average_duration_by_pair_hours = Trade_Analysis.rank_pairs_by_trade_duration(df)
      print('average_duration_by_pair_hours')
      print(average_duration_by_pair_hours)
      print('\n')


      # fig = px.bar(trade_counts_df, x='Symbol', y=['Profitable Trade Count', 'Loosing Trade Count'],
      #             title='Trade Counts by Symbol',
      #             labels={'value': 'Count', 'variable': 'Trade Type'})

      # chart_html = fig.to_html(full_html=False)
      # return chart_html
      fig = px.bar(average_duration_by_pair_hours, x='Symbol', y='Duration',
              title='Average Trade Duration by Symbol',
              labels={'value': 'Average Duration (hours)', 'variable': 'Symbol'})

      chart_html = fig.to_html(full_html=False)
      return chart_html