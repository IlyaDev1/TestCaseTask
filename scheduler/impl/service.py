from datetime import date, datetime, timedelta
from typing import List, Tuple

from .mappers import str_to_date, str_to_time, time_to_str


def find_day_or_emtpy_list(
    target_date: date, validated_days_list: list[dict]
) -> dict | None:
    """Находит день с совпадающей датой."""
    return next((d for d in validated_days_list if d["date"] == target_date), None)


def get_busy_slots(
    validated_days: list[dict], validated_timeslots: list[dict], date_value: str
) -> list[tuple[str, str]]:
    """
    Возвращает список занятых временных промежутков на указанную дату.

    Args:
        validated_days: Список словарей с данными рабочих дней (ключи: id, date, start, end).
        validated_timeslots: Список словарей с таймслотами (ключи: day_id, start, end).
        date_value: Строка с датой в формате "YYYY-MM-DD".

    Returns:
        Список занятых временных промежутков в виде кортежей строк.
        Если день не найден, возвращается пустой список.
    """
    target_date = str_to_date(date_value)

    day = find_day_or_emtpy_list(target_date, validated_days)
    if day is None:
        return []

    day_id = day["id"]
    return [
        (time_to_str(ts["start"]), time_to_str(ts["end"]))
        for ts in validated_timeslots
        if ts["day_id"] == day_id
    ]


def get_free_slots(
    days: list[dict], timeslots: list[dict], date_value: str
) -> List[Tuple[str, str]]:
    """
    Возвращает список свободных слотов на заданную дату.

    Args:
        days: список дней (dict с ключами: id, date, start, end)
        timeslots: список занятых слотов (day_id, start, end)
        date_value: дата в строке (формат YYYY-MM-DD)

    Returns:
        Список свободных слотов: [("HH:MM", "HH:MM"), ...]
    """
    target_date = str_to_date(date_value)

    day = find_day_or_emtpy_list(target_date, days)
    if day is None:
        return []

    day_start = day["start"]
    day_end = day["end"]

    day_timeslots = [ts for ts in timeslots if ts["day_id"] == day["id"]]

    free_slots = []
    current = day_start

    for slot in day_timeslots:
        if current < slot["start"]:
            free_slots.append((time_to_str(current), time_to_str(slot["start"])))
        current = max(current, slot["end"])

    if current < day_end:
        free_slots.append((time_to_str(current), time_to_str(day_end)))

    return free_slots


def is_available(
    date_value: str, start_time: str, end_time: str, days: list[dict], slots: list[dict]
) -> bool:
    """
    Проверяет, доступен ли указанный временной промежуток на дату.

    Args:
        date_value: Дата в формате "YYYY-MM-DD"
        start_time: Время начала в формате "HH:MM"
        end_time: Время окончания в формате "HH:MM"
        days: Список рабочих дней
        slots: Список рабочих слотов

    Returns:
        True, если промежуток доступен, иначе False
    """
    free_slots = get_free_slots(days, slots, date_value)

    start = str_to_time(start_time)
    end = str_to_time(end_time)

    for free_start_str, free_end_str in free_slots:
        free_start = str_to_time(free_start_str)
        free_end = str_to_time(free_end_str)

        if free_start <= start and end <= free_end:
            return True

    return False


def find_slot_for_duration(
    days: list[dict], timeslots: list[dict], duration_minutes: int
) -> tuple[str, str, str] | None:
    """
    Ищет первый подходящий свободный слот заданной длительности.

    Args:
        days: список словарей с данными о днях (id, date, start, end).
        timeslots: список словарей с занятыми слотами (day_id, start, end).
        duration_minutes: желаемая длительность слота в минутах.

    Returns:
        Кортеж (дата, время начала, время конца) или None, если слот не найден.
    """
    delta = timedelta(minutes=duration_minutes)

    for day in days:
        free_slots = get_free_slots(days, timeslots, day["date"].isoformat())
        for start_str, end_str in free_slots:
            start = datetime.strptime(start_str, "%H:%M")
            end = datetime.strptime(end_str, "%H:%M")
            if (end - start) >= delta:
                finish_time = (start + delta).time()
                return day["date"].isoformat(), start_str, time_to_str(finish_time)

    return None
