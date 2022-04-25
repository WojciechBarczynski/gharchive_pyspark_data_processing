import pandas as pd  # do not delete, it's used for DataFrame for repo_stats_pd_df
import utills
import spark_data_processing
import make_report


def main():
    repo_full_name, repo_short_name, year_string, month_string = utills.get_user_input()
    repo_owner = utills.get_repo_owner(repo_full_name)

    repo_stats_pd_df, failed_processing_pd_df = \
        spark_data_processing.get_stats(repo_full_name, year_string, month_string)

    make_report.generate_a_report\
        (repo_stats_pd_df, repo_owner, repo_short_name, month_string, year_string, failed_processing_pd_df)


if __name__ == '__main__':
    main()

