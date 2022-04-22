import wget


def get_repo_name(repo_url):
    name_list = repo_url.split('/')
    repo_name = name_list[-1]
    repo_owner = name_list[-2]
    return repo_name, repo_owner


def wget_file(url):
    file_name = wget.download(url)
    return file_name


def get_gh_archive_url(year, month, day, hour):
    return f"https://data.gharchive.org/{year}-{month}-{day}-{hour},json.gz"


def main():
    print(get_gh_archive_url('2015', '01', '01', '15'))


if __name__ == '__main__':

    main()

