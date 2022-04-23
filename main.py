import pyspark
import utills
import make_report
from pyspark.sql import SparkSession
import wget
import pandas as pd


def get_stats(repo_name, year, month):
    spark = SparkSession.builder.appName('github_repo_stats').getOrCreate()
    repo_stats_pd_df = pd.DataFrame(columns=['day', 'unique_watch_events', 'open_pull_request'])
    i = 0
    day = '01'

    watch_events_day_count = 0
    pull_request_events_day_count = 0

    for hour in range(24):
        hour_string = str(hour)
        if len(hour_string) == 1:
            hour_string += '0'
            hour_string = hour_string[::-1]
        gh_archive_url = f'https://data.gharchive.org/{year}-{month}-{day}-{hour_string},json.gz'

        json_url = wget.download(f'{gh_archive_url}')
        hour_gh_activity_spark_df = spark.read.json(json_url)
        hour_gh_activity_spark_df = hour_gh_activity_spark_df.select(['type', 'repo.name', 'actor.id'])
        hour_gh_activity_spark_df = hour_gh_activity_spark_df.filter(f'name == "{repo_name}"')
        pull_request_events_spark_df = hour_gh_activity_spark_df.filter('type == "PullRequestEvent"')
        watch_events_spark_df = hour_gh_activity_spark_df.filter('type == "WatchEvent"')
        watch_events_spark_df = watch_events_spark_df.select('id').distinct()

        pull_request_events_hour_count = pull_request_events_spark_df.count()
        watch_events_hour_count = watch_events_spark_df.count()
        
        pull_request_events_day_count += pull_request_events_hour_count
        watch_events_day_count += watch_events_hour_count
    
    repo_stats_pd_df.loc[i] = [f'{year}-{month}-{day}', watch_events_day_count, pull_request_events_day_count]
    i += 1

    '''
    df = spark.read.json()
    df = df.select(['type', 'repo.name', 'actor.id'])
    df = df.filter(f'name == "{repo_name}"')
    pr_events = df.filter('type == "PullRequestEvent"')
    watch_events = df.filter('type == "WatchEvent"')
    watch_events = watch_events.select('id').distinct()

    pr_events_count = pr_events.count()
    watch_events_count = watch_events.count()
    repo_stats_pd_df = pd.DataFrame(columns=['day', 'unique_watch_events', 'open_pull_request'])
    repo_stats_pd_df.loc[0] = [f'{year}-{month}-{day}', watch_events_count, pr_events_count]
    '''

    return repo_stats_pd_df


def main():
    print(get_stats('freeCodeCamp/freeCodeCamp', '2022', '01'))


if __name__ == '__main__':
    main()

