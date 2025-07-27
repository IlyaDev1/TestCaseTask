import asyncio

import pytest
import pytest_asyncio
from pytest_httpx import HTTPXMock

from scheduler import Scheduler
from scheduler.tests.schedules.schedule_dirty_instances import (
    correct_dirty_schedule,
    correct_dirty_schedule_by_url,
)
from scheduler.tests.schedules.schedule_instances import (
    correct_schedule_by_dict,
    correct_schedule_by_url,
)


@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    yield loop
    loop.close()


@pytest_asyncio.fixture(scope="session")
async def schedule_instance_by_url(httpx_mock: HTTPXMock):
    """Фикстура отдает асинхронно инициализированный объект расписания с URL."""
    mock_data: dict = correct_dirty_schedule_by_url

    httpx_mock.add_response(
        method="GET", url="https://ofc-test-01.tspb.su/test-task/", json=mock_data
    )

    scheduler = Scheduler()
    await scheduler.load_schedule_by_url(url="https://ofc-test-01.tspb.su/test-task/")
    yield scheduler


@pytest.fixture(scope="session")
def schedule_instance():
    """Фикстура возвращает уже обработанный словарь расписания."""
    yield correct_schedule_by_url


@pytest_asyncio.fixture
def schedule_instance_for_units():
    """Фикстура отдает асинхронно инициализированный объект с обычным расписанием."""
    scheduler = Scheduler()
    scheduler.load_schedule_by_dict(data=correct_dirty_schedule)
    yield scheduler
