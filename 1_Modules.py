import datetime
import random


def print_if_day_is_monday(date: datetime.date) -> None:
    """
    Print 'אין לי ויניגרט!' if the given date is monday.
    :param date: The date to be check.
    :return: None
    """
    if date.isoweekday() == 1:  # 1 = monday
        print("אין לי ויניגרט!")


def vinaigrette(start_date_str: str, end_date_str: str) -> datetime.date:
    """
    This function generates a random date between two given dates.
    :param start_date_str: The minimum date can be selected.
    :param end_date_str: The maximum date can be selected.
    :return: Random date between two given dates.
    """
    start_date = datetime.datetime.strptime(start_date_str, "%Y-%m-%d")
    end_date = datetime.datetime.strptime(end_date_str, "%Y-%m-%d")
    random_number_of_days = random.randrange((end_date - start_date).days)
    random_date = start_date + datetime.timedelta(random_number_of_days)
    print_if_day_is_monday(random_date)
    return random_date


if __name__ == "__main__":
    print(vinaigrette("1912-06-23", "1954-06-07"))

