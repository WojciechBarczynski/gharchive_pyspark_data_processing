import pandas as pd
import plotly.express as px
from utills import get_month_name
from dash import Dash, html, dcc


def get_bar_charts(repo_stat_pd_df):
    unique_watch_events_plot = px.bar(repo_stat_pd_df, x='day', y='watch_events_day_count',
                title='New stars count daily', template='plotly_dark',
                color='watch_events_day_count',
                labels={
                    'day': 'Date',
                    'watch_events_day_count': 'New stars count'
                })
    open_pull_requests = px.bar(repo_stat_pd_df, x='day', y='pull_request_events_day_count',
                                title='Opened pull requests count daily', template='plotly_dark',
                                color='pull_request_events_day_count',
                                labels={
                                    'day': 'Date',
                                    'pull_request_events_day_count': 'Opened pull requests'
                                })
    return unique_watch_events_plot, open_pull_requests


def generate_a_report(repo_stat_pd_df, repo_short_name, owner, year_string, month_string):
    print(repo_short_name)
    month_name = get_month_name(month_string)
    print(f'Report of activity at "{repo_short_name}" repository in {month_name}, {year_string}')
    print(f'Project name: "{repo_short_name}", Owner: "{owner}", Year: "{year_string}", Month: "{month_name}"')
    print(repo_stat_pd_df)
    repo_stat_pd_df.to_csv(f'report_of_activity_at_{repo_short_name}_repository_in_{month_name}_of_{year_string}.csv')

    unique_watch_events_plot, open_pull_requests = get_bar_charts(repo_stat_pd_df)

    app = Dash(__name__)

    app.layout = html.Div([
        html.H1(f'Report of activity at "{repo_short_name}" repository in {month_name}, {year_string}',
                style={'text-align': 'center'}),
        html.H2(f'Project name: "{repo_short_name}", Owner: "{owner}", Year: "{year_string}", Month: "{month_name}"',
                style={'text-align': 'center'}),

        dcc.Graph(
            id = 'watch_events_graph',
            figure = unique_watch_events_plot
        ),

        dcc.Graph(
            id = 'open_pull_requests_graph',
            figure = open_pull_requests
        )
    ])

    app.run_server()


repo_stat_df = pd.DataFrame(
    [['2020-01-01', 4, 1],
     ['2020-01-02', 3, 1],
     ['2020-01-03', 2, 1],
     ['2020-01-04', 1, 1],
     ['2020-01-05', 0, 1],
     ['2020-01-06', 0, 1],
     ['2020-01-07', 1, 1],
     ['2020-01-08', 0, 1],
     ['2020-01-09', 0, 1],
     ['2020-01-10', 1, 1],
     ['2020-01-11', 5, 0],
     ['2020-01-12', 2, 3],
     ['2020-01-13', 2, 1],
     ['2020-01-14', 3, 0],
     ['2020-01-15', 0, 0],
     ['2020-01-16', 1, 0],
     ['2020-01-17', 2, 2],
     ['2020-01-18', 1, 10],
     ['2020-01-19', 3, 0],
     ['2020-01-20', 0, 0],
     ['2020-01-21', 1, 0],
     ['2020-01-22', 0, 1],
     ['2020-01-23', 0, 0],
     ['2020-01-24', 5, 1],
     ['2020-01-25', 0, 1],
     ['2020-01-26', 1, 3],
     ['2020-01-27', 1, 1],
     ['2020-01-28', 3, 9],
     ['2020-01-29', 0, 4],
     ['2020-01-30', 1, 3],
     ['2020-01-31', 2, 1]],
    columns=['day', 'watch_events_day_count', 'pull_request_events_day_count']
)

if __name__ == '__main__':
    generate_a_report(repo_stat_df, 'freeCodeCamp', 'Jan Kowalski', '2020', '01')

