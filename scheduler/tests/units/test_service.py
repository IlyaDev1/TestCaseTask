import pytest

from scheduler.impl.service import get_busy_slots


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
