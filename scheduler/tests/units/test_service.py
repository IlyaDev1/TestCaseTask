import pytest

from scheduler.impl.service import (
    find_slot_for_duration,
    get_busy_slots,
    get_free_slots,
    is_available,
)


@pytest.mark.parametrize(
    "date_value, result",
    [
        (
            "2024-10-10",
            [("11:00", "12:00")],
        ),
        (
            "2025-10-10",
            [],
        ),
    ],
)
def test_get_busy_service(date_value, result, schedule_instance_for_units):
    days = schedule_instance_for_units.validated_days
    timeslots = schedule_instance_for_units.validated_timeslots

    func_result = get_busy_slots(days, timeslots, date_value)
    assert func_result == result


@pytest.mark.parametrize(
    "date_value, result",
    [
        (
            "2024-10-10",
            [("09:00", "11:00"), ("12:00", "18:00")],
        ),
        (
            "2025-10-10",
            [],
        ),
    ],
)
def test_get_free_service(date_value, result, schedule_instance_for_units):
    days = schedule_instance_for_units.validated_days
    timeslots = schedule_instance_for_units.validated_timeslots

    func_result = get_free_slots(days, timeslots, date_value)
    assert func_result == result


@pytest.mark.parametrize(
    "date_value, start_time, end_time, expected",
    [
        ("2024-10-10", "10:00", "10:30", True),  # попадает в свободный слот
        ("2024-10-10", "11:00", "11:30", False),  # попадает в занятый слот
        ("2025-10-10", "10:00", "11:00", False),  # такого дня нет
    ],
)
def test_is_available_service(
    date_value, start_time, end_time, expected, schedule_instance_for_units
):
    days = schedule_instance_for_units.validated_days
    timeslots = schedule_instance_for_units.validated_timeslots

    result = is_available(date_value, start_time, end_time, days, timeslots)
    assert result is expected


@pytest.mark.parametrize(
    "duration_minutes, expected",
    [
        (60, ("2024-10-10", "09:00", "10:00")),  # Первый слот 09:00–10:00
        (90, ("2024-10-10", "09:00", "10:30")),  # Первый подходящий — на след. день
        (300, ("2024-10-10", "12:00", "17:00")),  # 5 часов
        (600, None),  # Слишком большая длительность
    ],
)
def test_find_slot_for_duration(
    duration_minutes, expected, schedule_instance_for_units
):
    days = schedule_instance_for_units.validated_days
    timeslots = schedule_instance_for_units.validated_timeslots

    result = find_slot_for_duration(days, timeslots, duration_minutes)
    assert result == expected
