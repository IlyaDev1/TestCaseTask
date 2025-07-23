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


@pytest.fixture
async def schedule_instance_by_url(httpx_mock: HTTPXMock):
    """Фикстура отдает асинхронно инициализированный объект расписания с URL."""
    mock_data: dict = correct_dirty_schedule_by_url

    httpx_mock.add_response(
        method="GET", url="https://ofc-test-01.tspb.su/test-task/", json=mock_data
    )

    scheduler = Scheduler()
    await scheduler.load_schedule_by_url_or_dict(
        url="https://ofc-test-01.tspb.su/test-task/"
    )
    return scheduler


@pytest.fixture(scope="session")
def schedule_instance():
    """Фикстура возвращает уже обработанный словарь расписания."""
    return correct_schedule_by_url


@pytest_asyncio.fixture
async def schedule_instance_for_units():
    """Фикстура отдает асинхронно инициализированный объект с обычным расписанием."""
    scheduler = Scheduler()
    await scheduler.load_schedule_by_url_or_dict(data=correct_dirty_schedule)
    yield scheduler
