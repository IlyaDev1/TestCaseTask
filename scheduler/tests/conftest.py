import pytest
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


@pytest.fixture(scope="function")
def schedule_instance_by_url(httpx_mock: HTTPXMock):
    """Фикстура отдает объект расписания с url."""

    mock_data: dict = correct_dirty_schedule_by_url

    httpx_mock.add_response(
        method="GET", url="https://ofc-test-01.tspb.su/test-task/", json=mock_data
    )

    yield Scheduler(url="https://ofc-test-01.tspb.su/test-task/")


@pytest.fixture(scope="session")
def schedule_instance():
    """Эта фисктура отдает уже готовый и обработанный объект расписания
    Нужен, чтобы постоянно не вызывать долгий schedule_instance_by_url
    """

    yield correct_schedule_by_url


@pytest.fixture(scope="session")
def schedule_instance_for_units():
    """Эта фикстура будет отдавать schedule объект с известным обычным расписанием."""

    yield Scheduler(data=correct_dirty_schedule)
