from pprint import pprint

import pytest
from pytest_httpx import HTTPXMock

from scheduler import Scheduler
from scheduler.impl.schedule_loader.exceptions import (
    EmptyLoadDataError,
    LoadByURLError,
    ScheduleKeysError,
    ScheduleValuesError,
    TimeSlotStructureError,
    URLOrDataOnlyError,
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
    await scheduler.load_schedule_by_url_or_dict(
        url="https://ofc-test-01.tspb.su/test-task/"
    )

    assert scheduler.schedule == correct_schedule_by_url


@pytest.mark.asyncio
async def test_correct_load_by_dict():
    """Тест проверяет, что c dict данные загружаются корректно."""

    scheduler = Scheduler()
    await scheduler.load_schedule_by_url_or_dict(data=correct_dirty_schedule)

    assert scheduler.schedule == correct_schedule_by_dict


@pytest.mark.asyncio
async def test_empty_args():
    """Тест проверяет вызов ошибки EmptyLoadDataError."""

    scheduler = Scheduler()
    with pytest.raises(EmptyLoadDataError, match="Either url or data must be provided"):
        await scheduler.load_schedule_by_url_or_dict()


@pytest.mark.asyncio
async def test_url_and_data_exist():
    """Тест проверяет вызов ошибки URLOrDataOnlyError."""

    scheduler = Scheduler()
    with pytest.raises(URLOrDataOnlyError, match="Provide only one of url or data"):
        await scheduler.load_schedule_by_url_or_dict(
            url="https://ofc-test-01.tspb.su/test-task/",
            data={"days": [], "timeslots": []},
        )


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
        await scheduler.load_schedule_by_url_or_dict(
            url="https://ofc-test-01.tspb.su/test-task/"
        )


@pytest.mark.asyncio
async def test_timeslots_beyond_work_time():
    """Тест проверяет вызов ошибки TimeSlotStructureError, если таймслот вне рабочего времени."""

    scheduler = Scheduler()
    with pytest.raises(TimeSlotStructureError, match="outside of work hours"):
        await scheduler.load_schedule_by_url_or_dict(
            data=schedule_with_timeslot_beyond_work_time
        )
