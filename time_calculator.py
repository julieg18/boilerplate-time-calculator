from datetime import datetime, timedelta
import re


def get_hours_and_minutes(time):
    hours, minutes = re.findall(r'\d+', time)
    hours = int(hours) + 12 if time.endswith('PM') else int(hours)
    minutes = int(minutes)
    return hours, minutes


def get_formatted_time(date, weekday_name, days_difference):
    hour = date.hour
    if hour > 12:
        hour -= 12
    elif hour == 0:
        hour = 12

    minute = f'0{date.minute}' if date.minute < 10 else date.minute

    abbr = 'AM' if date.hour < 12 else 'PM'

    weekday = f', {weekday_name.capitalize()}' if weekday_name != 'not_given' else ''

    days_later = ''
    if days_difference == 1:
        days_later = ' (next day)'
    elif days_difference > 0:
        days_later = f' ({days_difference} days later)'

    return f'{hour}:{minute} {abbr}{weekday}{days_later}'


def add_time(start, duration, day='not_given'):
    days_of_week = ['monday', 'tuesday',
                    'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    day_of_month = days_of_week.index(
        day.lower() if day != 'not_given' else 'monday') + 1

    start_hours, start_minutes = get_hours_and_minutes(start)
    duration_hours, duration_minutes = get_hours_and_minutes(duration)

    start_date = datetime(year=2018, month=1, day=day_of_month,
                          hour=start_hours, minute=start_minutes)
    delta = timedelta(hours=+duration_hours, minutes=+duration_minutes)
    result_date = start_date + delta
    rounded_start = start_date.replace(
        hour=0, minute=0, second=0, microsecond=0)
    rounded_result = result_date.replace(
        hour=0, minute=0, second=0, microsecond=0)
    difference = rounded_result-rounded_start

    weekday_name = days_of_week[result_date.weekday(
    )] if day != 'not_given' else day

    return get_formatted_time(result_date, weekday_name, difference.days)
