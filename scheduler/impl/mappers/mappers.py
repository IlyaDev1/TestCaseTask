from datetime import date, datetime, time

from .exceptions import DateFormatError, TimeFormatError


def str_to_date(date_str: str) -> date:
    try:
        target_date: date = datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError as e:
        raise DateFormatError("Date must be in YYYY-MM-DD format") from e
    else:
        return target_date


def str_to_time(time_str: str) -> time:
    try:
        target_time: time = datetime.strptime(time_str, "%H:%M").time()
    except ValueError as e:
        raise TimeFormatError("Time must be in HH:MM format") from e
    else:
        return target_time
