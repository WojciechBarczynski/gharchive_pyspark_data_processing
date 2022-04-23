def get_user_input():
    print('This is a program to create a report of basic stats for public GitHub repo from chosen month.')
    print('Please type public repo name (e.g. freeCodeCamp/freeCodeCamp): ')
    repo_full_name = input()
    repo_full_name = repo_full_name.strip()
    repo_short_name = repo_full_name.split('/')
    repo_short_name = repo_short_name[0]
    print('Please type year (e.g. 2021): ')
    year_string = input()
    year_string = year_string.strip()
    print('Please type chosen month (e.g. 01): ')
    month_string = input()
    month_string = month_string.strip()
    month_string = month_string.lower()
    if month_string == 'january' or month_string == 'jan'or month_string == '1':
        month_string = '01'
    elif month_string == 'february' or month_string == 'feb' or month_string == '2':
        month_string = '02'
    elif month_string == 'march' or month_string == 'mar' or month_string == '3':
        month_string = '03'
    elif month_string == 'april' or month_string == 'apr' or month_string == '4':
        month_string = '04'
    elif month_string == 'may' or month_string == '5':
        month_string = '05'
    elif month_string == 'june' or month_string == 'jun' or month_string == '6':
        month_string = '06'
    elif month_string == 'july' or month_string == 'jul' or month_string == '7':
        month_string = '07'
    elif month_string == 'august' or month_string == 'aug' or month_string == '8':
        month_string = '08'
    elif month_string == 'september' or month_string == 'sep' or month_string == '9':
        month_string = '09'
    elif month_string == 'october' or month_string == 'oct':
        month_string = '10'
    elif month_string == 'november' or month_string == 'nov':
        month_string = '11'
    elif month_string == 'december' or month_string == 'dec':
        month_string = '12'
    return repo_full_name, repo_short_name, year_string, month_string


def get_repo_owner(repo_name):
    repo_owner = repo_name.split('/')
    repo_owner = repo_owner[0]
    return repo_owner


def get_number_of_days_in_month(month_string, year_string):
    if month_string == '01' or month_string == '03' or month_string == '05' or month_string == '07' or month_string == '08' or month_string == '10' or month_string == '12':
        return 31
    if month_string == '02':
        year = int(year_string)
        if year % 4 == 0:
            return 29
        else:
            return 28
    else:
        return 30


def get_month_name(month):
    if month == '01':
        return 'January'
    elif month == '02':
        return 'February'
    elif month == '03':
        return 'March'
    elif month == '04':
        return 'April'
    elif month == '05':
        return 'May'
    elif month == '06':
        return 'June'
    elif month == '07':
        return 'July'
    elif month == '08':
        return 'August'
    elif month == '09':
        return 'September'
    elif month == '10':
        return 'October'
    elif month == '11':
        return 'November'
    else:
        return 'December'

