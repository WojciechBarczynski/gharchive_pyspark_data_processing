import pandas as pd
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html

def plot(df):
    unique_watch_events_plot = px.bar(df, x='day', y='unique_watch_events',
                title='unique watch events daily', template='plotly_dark',
                color='unique_watch_events',
                labels={
                    'day': 'date',
                    'unique_watch_events': 'unique watch events'
                })
    open_pull_requests = px.bar(df, x='day', y='open_pull_requests',
                                title='open pull requests daily', template='plotly_dark',
                                color='open_pull_requests',
                                labels={
                                    'day': 'date',
                                    'open_pull_requests': 'open pull requests'
                                })
    return unique_watch_events_plot, open_pull_requests


def generate_a_report(repo_name, year, month, df):
    unique_watch_events_plot, open_pull_requests = plot(df)

    app.layout = html.Div([
        html.H1(f'Report of activity at {repo_name} repository in {month}, {year}',
                style={'text-align': 'center'}),

    ])

df = pd.DataFrame(
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
    columns=['day', 'unique_watch_events', 'open_pull_requests']
)

plot(df)