#! usr/bin/python3

from datetime import date
import datetime
#import jdatetime


def calculate_age_year(day, month, year):
    """calculate age in year

    Args:
        day (int): birthday day
        month (int): birthday month
        year (int): birthday year

    Returns:
        age: in year
    """
    today = date.today()
    birthdate = date(year, month, day)
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age


def age_in_seconds(year: int, month: int, day: int, hour: int, minute: int, second:int) -> int: 
    """calculate age in seconds

    Args:
        day (int): birthday day
        month (int): birthday month
        year (int): birthday year
        hour (int): birthday hour
        minute (int): birthday minute
        seconds (int): birthday seconds

    Returns:
        age: in seconds
    """
    today_now = datetime.datetime.now()
    year_second = calculate_age_year(day, month, year)*365*24*3600
    if today_now.month - month < 0:
        month_seconds = (12 + (today_now.month - month))*30*24*3600
    else:
        month_seconds = (today_now.month - month)*30*24*3600

    day_second = ((30 - day) + today_now.day)*24*3600
    hour_second = ((24 - hour) + today_now.hour)*3600
    minute_second = ((60 - minute) + today_now.minute)*60
    seconds = (60 - second) + today_now.second
    return year_second + month_seconds + day_second + hour_second + minute_second + seconds

def days_minutes_next_birthday(year: int, month: int, day: int, hour: int, minute: int, second:int) -> int:
    """_summary_

    Args:
        day (int): birthday day
        month (int): birthday month
        year (int): birthday year
        hour (int): birthday hour
        minute (int): birthday minute
        seconds (int): birthday seconds

    Returns:
        int: days and minutes to next birthday
    """
    year_in_seconds = 365*24*3600
    today = datetime.datetime.now()
    if today.month > month:
        last_birthday_month_in_days = (today.month - month)*30
    else:
        last_birthday_month_in_days = (12 + (today.month - month))*30
    
    last_birthday_day_in_days = (30 - day) + today.day
    last_birthday_minutes = ((24 - hour)+today.hour)*60 + (60 - minute) + today.minute

    days_to_next_birthday = (365 - last_birthday_day_in_days)
    return days_to_next_birthday

# def fromgregorian(year: int, month: int, day: int) -> int:
    """
    from georgian to jalali date
    """
#     return jdatetime.date.fromgregorian(day,month,year)




    
    


    

      
