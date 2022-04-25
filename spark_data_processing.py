import pyspark
import utills
import os
from pyspark.sql import SparkSession
import pandas as pd


def get_stats(repo_name, year_string, month_string):
    failed_processing_pd_df = pd.DataFrame(columns=['date'])
    failed_processing_index = 0
    spark = SparkSession.builder.appName('github_repo_stats').getOrCreate()
    repo_stats_pd_df = pd.DataFrame(columns=['day', 'watch_events_day_count', 'pull_request_events_day_count'])
    day_index = 0

    days_in_month = utills.get_number_of_days_in_month(month_string, year_string)

    for day in range(1, days_in_month + 1):
        day_string = str(day)
        if len(day_string) == 1:
            day_string += '0'
            day_string = day_string[::-1]

        watch_events_day_count = 0
        pull_request_events_day_count = 0

        for hour in range(24):
            hour_string = str(hour)
            gh_archive_url = \
                f'https://data.gharchive.org/{year_string}-{month_string}-{day_string}-{hour_string}.json.gz'

            try:
                os.system(f'wget {gh_archive_url}')
            except:
                failed_processing_pd_df.loc[failed_processing_index] = \
                    [f'{year_string}-{month_string}-{day_string}-{hour_string}']
                failed_processing_index += 1
                continue

            json_url = f'{year_string}-{month_string}-{day_string}-{hour}.json.gz'

            try:
                hour_gh_activity_spark_df = spark.read.json(json_url)
            except:
                failed_processing_pd_df.loc[failed_processing_index] = \
                    [f'{year_string}-{month_string}-{day_string}-{hour_string}']
                failed_processing_index += 1
                continue

            hour_gh_activity_spark_df = hour_gh_activity_spark_df.select(['type', 'repo.name', 'actor.id'])
            hour_gh_activity_spark_df = hour_gh_activity_spark_df.filter(f'name == "{repo_name}"')
            pull_request_events_spark_df = hour_gh_activity_spark_df.filter('type == "PullRequestEvent"')
            watch_events_spark_df = hour_gh_activity_spark_df.filter('type == "WatchEvent"')
            watch_events_spark_df = watch_events_spark_df.select('id').distinct()

            pull_request_events_day_count += pull_request_events_spark_df.count()
            watch_events_day_count += watch_events_spark_df.count()

            os.remove(json_url)

        repo_stats_pd_df.loc[day_index] = [f'{year_string}-{month_string}-{day_string}', watch_events_day_count,
                                           pull_request_events_day_count]
        day_index += 1

    return repo_stats_pd_df, failed_processing_pd_df

