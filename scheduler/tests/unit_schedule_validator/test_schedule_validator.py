from datetime import date, time

import pytest

from scheduler.impl.schedule_loader.exceptions import (
    DayStructureError,
    TimeSlotStructureError,
)
from scheduler.impl.schedule_loader.schedule_validator import ScheduleValidator


def test_days_validator_valid():
    days = [
        {
            "id": 1,
            "date": "2025-01-01",
            "start": "09:00",
            "end": "17:00",
        }
    ]
    result = ScheduleValidator.days_validator(days)
    assert result == [
        {
            "id": 1,
            "date": date(2025, 1, 1),
            "start": time(9, 0),
            "end": time(17, 0),
        }
    ]


@pytest.mark.parametrize(
    "bad_day",
    [
        "not a dict",
        {"id": 1, "date": "2025-01-01", "start": "09:00"},  # missing end
        {"id": "1", "date": "2025-01-01", "start": "09:00", "end": "17:00"},  # id str
        {
            "id": 1,
            "date": "01-01-2025",
            "start": "09:00",
            "end": "17:00",
        },  # wrong date format
        {
            "id": 1,
            "date": "2025-01-01",
            "start": "17:00",
            "end": "09:00",
        },  # end < start
        {
            "id": 1,
            "date": "2025-01-01",
            "start": "xx:yy",
            "end": "17:00",
        },  # invalid time
    ],
)
def test_days_validator_invalid(bad_day):
    with pytest.raises(DayStructureError):
        ScheduleValidator.days_validator([bad_day])


def test_timeslots_validator_valid():
    timeslots = [
        {
            "id": 1,
            "day_id": 1,
            "start": "10:00",
            "end": "11:00",
        }
    ]
    result = ScheduleValidator.timeslots_validator(timeslots, {1})
    assert result == [
        {
            "id": 1,
            "day_id": 1,
            "start": time(10, 0),
            "end": time(11, 0),
        }
    ]


@pytest.mark.parametrize(
    "bad_slot",
    [
        "not a dict",
        {"id": 1, "day_id": 1, "start": "10:00"},  # missing end
        {"id": "1", "day_id": 1, "start": "10:00", "end": "11:00"},  # id str
        {"id": 1, "day_id": "1", "start": "10:00", "end": "11:00"},  # day_id str
        {"id": 1, "day_id": 999, "start": "10:00", "end": "11:00"},  # unknown day_id
        {"id": 1, "day_id": 1, "start": "12:00", "end": "11:00"},  # start > end
        {"id": 1, "day_id": 1, "start": "bad", "end": "11:00"},  # invalid time
    ],
)
def test_timeslots_validator_invalid(bad_slot):
    with pytest.raises(TimeSlotStructureError):
        ScheduleValidator.timeslots_validator([bad_slot], {1})
