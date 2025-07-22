import pytest
from pytest_httpx import HTTPXMock

from scheduler import Scheduler
from scheduler.impl.schedule_loader.exceptions import (
    EmptyLoadDataError,
    LoadByURLError,
    ScheduleKeysError,
    URLOrDataOnlyError,
)
from scheduler.tests.schedules.schedule_dirty_instances import (
    correct_dirty_schedule,
    schedule_with_bad_keys,
)
from scheduler.tests.schedules.schedule_instances import (
    correct_schedule_by_dict,
    correct_schedule_by_url,
)


def test_correct_load_by_url(schedule_instance_by_url: Scheduler):
    """Тест проверяет, что c url данные загружаются корректно."""

    assert schedule_instance_by_url.schedule == correct_schedule_by_url


def test_correct_load_by_dict():
    """Тест проверяет, что c dict данные загружаются корректно."""

    scheduler = Scheduler(data=correct_dirty_schedule)
    assert scheduler.schedule == correct_schedule_by_dict


def test_empty_args():
    """Тест проверяет вызов ошибки EmptyLoadDataError."""

    with pytest.raises(EmptyLoadDataError, match="Either url or data must be provided"):
        Scheduler()


def test_url_and_data_exist():
    """Тест проверяет вызов ошибки URLOrDataOnlyError."""

    with pytest.raises(URLOrDataOnlyError, match="Provide only one of url or data"):
        Scheduler(url="https", data={"data": [dict()]})


def test_load_by_url_error(httpx_mock: HTTPXMock):
    """Тест проверяет вызов ошибки LoadByURLError."""

    httpx_mock.add_response(
        method="GET",
        url="https://ofc-test-01.tspb.su/test-task/",
        status_code=404,
    )

    with pytest.raises(LoadByURLError, match="Failed to load schedule from URL:"):
        Scheduler(url="https://ofc-test-01.tspb.su/test-task/")


def test_schedule_keys_error():
    """Тест проверяет вызов ошибки ScheduleKeysError."""

    with pytest.raises(ScheduleKeysError, match="('days', 'timeslots')"):
        Scheduler(data=schedule_with_bad_keys)
