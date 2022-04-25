import pandas as pd
import make_report


def main():
    print('Please select demo report: ')
    print('1. Report of activity at freeCodeCamp/freeCodeCamp repo in January of 2022 (type 1)')
    print('2. Report of activity at kubernetes/kubernetes repo in February of 2022 (type 2)')
    print('3. Report of activity at tensorflow/tensorflow repo in April of 2021 (type 3)')
    print('4. Report of activity at facebook/react repo in September of 2017 (type 4)')
    print('5. Report of activity at docker/docker repo in December of 2016 (type 5)')
    option = input()
    failed_processing_pd_df = pd.DataFrame(columns=['date'])
    columns_list = ['day', 'watch_events_day_count', 'pull_request_events_day_count']
    if option == '1':
        repo_stat_pd_df = pd.read_csv(
            'examples/report_of_activity_at_freeCodeCamp_freeCodeCamp_repository_in_January_of_2022.csv',
            usecols=columns_list)
        make_report.generate_a_report(
            repo_stat_pd_df, 'freeCodeCamp', 'freeCodeCamp', '01', '2022', failed_processing_pd_df)
    elif option == '2':
        repo_stat_pd_df = pd.read_csv(
            'examples/report_of_activity_at_kubernetes_kubernetes_repository_in_February_of_2022.csv',
            usecols=columns_list)
        make_report.generate_a_report(repo_stat_pd_df, 'kubernetes', 'kubernetes', '02', '2022',
                                      failed_processing_pd_df)
    elif option == '3':
        repo_stat_pd_df = pd.read_csv(
            'examples/report_of_activity_at_tensorflow_tensorflow_repository_in_April_of_2021.csv',
            usecols=columns_list)
        make_report.generate_a_report(repo_stat_pd_df, 'tensorflow', 'tensorflow', '04', '2021',
                                      failed_processing_pd_df)
    elif option == '4':
        repo_stat_pd_df = pd.read_csv(
            'examples/report_of_activity_at_facebook_react_repository_in_September_of_2017.csv',
            usecols=columns_list)
        make_report.generate_a_report(repo_stat_pd_df, 'facebook', 'react', '09', '2017',
                                      failed_processing_pd_df)
    elif option == '5':
        repo_stat_pd_df = pd.read_csv(
            'examples/report_of_activity_at_docker_docker_repository_in_December_of_2016.csv',
            usecols=columns_list)
        make_report.generate_a_report(repo_stat_pd_df, 'docker', 'docker', '12', '2016',
                                      failed_processing_pd_df)
    else:
        print('Option not supported. Try again')
        main()


if __name__ == '__main__':
    main()