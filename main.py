import pyspark
import utills
import make_report
import os
from pyspark.sql import SparkSession
import wget
import pandas as pd


def get_stats(repo_name, year_string, month_string):
    spark = SparkSession.builder.appName('github_repo_stats').getOrCreate()
    repo_stats_pd_df = pd.DataFrame(columns=['day', 'watch_events_day_count', 'pull_request_events_day_count'])
    i = 0

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
            gh_archive_url = f'https://data.gharchive.org/{year_string}-{month_string}-{day_string}-{hour_string}.json.gz'
            print(gh_archive_url)

            os.system(f'wget {gh_archive_url}')

            json_url = f'{year_string}-{month_string}-{day_string}-{hour}.json.gz'
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

            os.remove(json_url)
    
        repo_stats_pd_df.loc[i] = [f'{year_string}-{month_string}-{day_string}', watch_events_day_count, pull_request_events_day_count]
        i += 1
    return repo_stats_pd_df


def main():
    repo_full_name, repo_short_name, year_string, month_string = utills.get_user_input()
    repo_owner = utills.get_repo_owner(repo_full_name)
    repo_stats_pd_df = get_stats(repo_full_name, year_string, month_string)
    make_report.generate_a_report(repo_stats_pd_df, repo_short_name, repo_owner, year_string, month_string)


if __name__ == '__main__':
    main()

