from requests import RequestException, get

from .exceptions import (
    EmptyLoadDataError,
    LoadByURLError,
    ScheduleKeysError,
    ScheduleValuesError,
    URLOrDataOnlyError,
)
from .schedule_validator import ScheduleValidator


def check_and_make_schedule_structure(data: dict) -> dict[str, list]:
    """Проверяет и преобразует структуру данных расписания.

    Args:
        data: Словарь с данными расписания.

    Returns:
        Словарь с валидированными днями и таймслотами.

    Raises:
        ScheduleKeysError: Если ключи словаря некорректны.
        ScheduleValuesError: Если days или timeslots не списки.
        DayStructureError: Если структура дней некорректна.
        TimeSlotStructureError: Если структура таймслотов некорректна.
    """
    if not ScheduleValidator.is_keys_correct(data):
        raise ScheduleKeysError(
            f"Keys {data.keys()} are incorrect, required: ('days', 'timeslots')"
        )

    days = data.get("days")
    timeslots = data.get("timeslots")

    if not ScheduleValidator.is_days_timeslots_list(days, timeslots):
        raise ScheduleValuesError("days and timeslots must be lists")

    validated_days = ScheduleValidator.days_validator(days)
    day_ids = {day["id"] for day in validated_days}
    validated_timeslots = ScheduleValidator.timeslots_validator(timeslots, day_ids)

    return {"days": validated_days, "timeslots": validated_timeslots}


def url_loader(url: str) -> dict[str, list]:
    """Загружает данные расписания по URL.

    Args:
        url: URL API для получения данных.

    Returns:
        Словарь с данными расписания.

    Raises:
        LoadByURLError: Если не удалось загрузить данные по URL.
    """
    try:
        response = get(url)
        data = response.json()
        return check_and_make_schedule_structure(data)
    except RequestException as e:
        raise LoadByURLError(f"Failed to load schedule from URL: {e}")


def load_schedule(url: str | None = None, data: dict | None = None) -> dict[str, list]:
    """Загружает данные расписания через API или из словаря.

    Args:
        url: URL API для получения данных о расписании.
        data: Данные о расписании в формате {"days": [...], "timeslots": [...]}.

    Returns:
        Словарь с валидированными данными расписания.

    Raises:
        EmptyLoadDataError: Если не передан ни url, ни data.
        URLOrDataOnlyError: Если переданы оба аргумента: url и data.
        LoadByURLError: Если не удалось загрузить данные по URL.
        ScheduleKeysError: Если ключи словаря некорректны.
        ScheduleValuesError: Если days или timeslots не списки.
        DayStructureError: Если структура дней некорректна.
        TimeSlotStructureError: Если структура таймслотов некорректна.
    """
    if url is None and data is None:
        raise EmptyLoadDataError("Either url or data must be provided")
    elif url is not None and data is not None:
        raise URLOrDataOnlyError("Provide only one of url or data")
    elif url is not None:
        return url_loader(url)
    elif data is not None:
        return check_and_make_schedule_structure(data)
    else:
        return {}
