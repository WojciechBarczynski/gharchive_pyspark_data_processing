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


def generate_report(repo_stat_pd_df, owner, repo_short_name, month_string, year_string, failed_processing_pd_df):
    month_name = get_month_name(month_string)
    print(f'Report of activity at "{repo_short_name}" repository in {month_name} {year_string}')
    print(f'Project name: "{repo_short_name}", Owner: "{owner}", Year: "{year_string}", Month: "{month_name}"')
    print(repo_stat_pd_df)

    if not failed_processing_pd_df.empty:
        print('Failed to process data from:')
        print(failed_processing_pd_df)
        failed_processing_pd_df.to_csv(
            f'failed_processing_at_{owner}_{repo_short_name}_repository_in_{month_name}_of_{year_string}.csv')

    repo_stat_pd_df.to_csv(
        f'report_of_activity_at_{owner}_{repo_short_name}_repository_in_{month_name}_of_{year_string}.csv')

    unique_watch_events_plot, open_pull_requests = get_bar_charts(repo_stat_pd_df)

    app = Dash(__name__)

    app.layout = html.Div([
        html.H1(f'Report of activity at "{repo_short_name}" repository in {month_name} {year_string}',
                style={'text-align': 'center'}),
        html.H2(f'Project name: "{repo_short_name}", Owner: "{owner}", Year: "{year_string}", Month: "{month_name}"',
                style={'text-align': 'center'}),

        dcc.Graph(
            id='watch_events_graph',
            figure=unique_watch_events_plot
        ),

        dcc.Graph(
            id='open_pull_requests_graph',
            figure=open_pull_requests
        )
    ])

    app.run_server()


