def get_user_input():
    print('This is a program to create a report of basic stats for public GitHub repo from chosen month.')
    print('Please type public repo url (e.g. https://github.com/apache/spark): ')
    repo_url = input()
    repo_url = repo_url.strip()
    print('Please type year (e.g. 2021): ')
    year = input()
    year = year.strip()
    print('Please type chosen month (e.g. 01): ')
    month = input()
    month = month.strip()
    month = month.lower()
    if month == 'january' or month == 'jan'or month == '1':
        month = '01'
    elif month == 'february' or month == 'feb' or month == '2':
        month = '02'
    elif month == 'march' or month == 'mar' or month == '3':
        month = '03'
    elif month == 'april' or month == 'apr' or month == '4':
        month = '04'
    elif month == 'may' or month == '5':
        month = '05'
    elif month == 'june' or month == 'jun' or month == '6':
        month = '06'
    elif month == 'july' or month == 'jul' or month == '7':
        month = '07'
    elif month == 'august' or month == 'aug' or month == '8':
        month = '08'
    elif month == 'september' or month == 'sep' or month == '9':
        month = '09'
    elif month == 'october' or month == 'oct':
        month = '10'
    elif month == 'november' or month == 'nov':
        month = '11'
    elif month == 'december' or month == 'dec':
        month = '12'
    return repo_url, year, month


def get_number_of_days_in_month(month, year):
    if month == '01' or month == '03' or month == '05' or month == '07' or month == '08' or month == '10' or month == '12':
        return 31
    if month == '02':
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

