import pytest
from pytest_httpx import HTTPXMock

from scheduler import Scheduler
from scheduler.impl.schedule_loader.exceptions import (
    LoadByURLError,
    TimeSlotStructureError,
)
from scheduler.tests.schedules.schedule_dirty_instances import (
    correct_dirty_schedule,
    correct_dirty_schedule_by_url,
    schedule_with_timeslot_beyond_work_time,
)
from scheduler.tests.schedules.schedule_instances import (
    correct_schedule_by_dict,
    correct_schedule_by_url,
)


@pytest.mark.asyncio
async def test_correct_load_by_url(httpx_mock: HTTPXMock):
    """Тест проверяет, что c url данные загружаются корректно."""

    httpx_mock.add_response(
        method="GET",
        url="https://ofc-test-01.tspb.su/test-task/",
        json=correct_dirty_schedule_by_url,
    )

    scheduler = Scheduler()
    await scheduler.load_schedule_by_url(url="https://ofc-test-01.tspb.su/test-task/")

    assert scheduler.schedule == correct_schedule_by_url


def test_correct_load_by_dict():
    """Тест проверяет, что c dict данные загружаются корректно."""

    scheduler = Scheduler()
    scheduler.load_schedule_by_dict(data=correct_dirty_schedule)

    assert scheduler.schedule == correct_schedule_by_dict


@pytest.mark.asyncio
async def test_load_by_url_error(httpx_mock: HTTPXMock):
    """Тест проверяет вызов ошибки LoadByURLError."""

    httpx_mock.add_response(
        method="GET",
        url="https://ofc-test-01.tspb.su/test-task/",
        status_code=404,
    )

    scheduler = Scheduler()
    with pytest.raises(LoadByURLError, match="Failed to load schedule from URL:"):
        await scheduler.load_schedule_by_url(
            url="https://ofc-test-01.tspb.su/test-task/"
        )


def test_timeslots_beyond_work_time():
    """Тест проверяет вызов ошибки TimeSlotStructureError, если таймслот вне рабочего времени."""

    scheduler = Scheduler()
    with pytest.raises(TimeSlotStructureError, match="outside of work hours"):
        scheduler.load_schedule_by_dict(data=schedule_with_timeslot_beyond_work_time)
