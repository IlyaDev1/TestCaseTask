import pytest
from pytest_httpx import HTTPXMock

from scheduler import Scheduler

from .schedule_dirty_instances import correct_dirty_schedule_by_url
from .schedule_instances import correct_schedule_by_url


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
