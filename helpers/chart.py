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

        fig = px.bar(average_duration_by_pair_hours, x='Symbol', y='Duration',
                title='Average Trade Duration by Symbol (hours)',
                labels={'value': 'Average Duration (hours)', 'variable': 'Symbol'})

        chart_html = fig.to_html(full_html=False)
        return chart_html
    


    def generate_profit_per_day_by_symbol(df):
        profit_per_day = Trade_Analysis.calculate_profit_per_day_of_holding_time(df)

        fig = px.bar(profit_per_day, x='Symbol', y='Average Profit per Day',
                title='Profit per Day by Symbol',
                labels={'value': 'Average Profit per Day', 'variable': 'Symbol'})

        chart_html = fig.to_html(full_html=False)
        return chart_html
    




    def generate_total_net_profit_by_symbol(df):
        total_net_profit_per_pair = Trade_Analysis.rank_pairs_by_total_net_profit(df)

        fig = px.bar(total_net_profit_per_pair, x='Symbol', y='Total Net Profit',
                title='Total Net Profit by Symbol',
                labels={'value': 'Total Net Profit', 'variable': 'Symbol'})

        chart_html = fig.to_html(full_html=False)
        return chart_html