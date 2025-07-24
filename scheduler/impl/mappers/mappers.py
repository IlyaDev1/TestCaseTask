from datetime import date, datetime, time

from .exceptions import DateFormatError, TimeFormatError


def str_to_date(date_value: str) -> date:
    try:
        target_date: date = datetime.strptime(date_value, "%Y-%m-%d").date()
    except ValueError as e:
        raise DateFormatError("Date must be in YYYY-MM-DD format") from e
    else:
        return target_date


def str_to_time(time_value: str) -> time:
    try:
        target_time: time = datetime.strptime(time_value, "%H:%M").time()
    except ValueError as e:
        raise TimeFormatError("Time must be in HH:MM format") from e
    else:
        return target_time


def time_to_str(time_value: time) -> str:
    return time_value.strftime("%H:%M")
