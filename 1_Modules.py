import datetime
import random


def vinaigrette(start_date_str, end_date_str):
    '''
    this function generates a random date between two given dates
    :param start_date_str: the minimum date ro be selected
    :param end_date_str: the maximum date ro be selected
    :return: random date between two given dates
    '''
    list_dates = start_date_str.split("-")
    start_date = datetime.date(int(list_dates[0]), int(list_dates[1]), int(list_dates[2]))
    list_dates = end_date_str.split("-")
    end_date = datetime.date(int(list_dates[0]), int(list_dates[1]), int(list_dates[2]))
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    if random_date.isoweekday() == 1:  # 1 = monday
        print("אין לי ויניגרט!")
    return random_date

print(vinaigrette("1912-06-23", "1954-06-07"))