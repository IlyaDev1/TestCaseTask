import pytest

from scheduler import Scheduler
from scheduler.impl.schedule_loader.exceptions import (
    EmptyLoadDataError,
    URLOrDataOnlyError,
)
from scheduler.tests.schedules.schedule_dirty_instances import correct_dirty_schedule
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
    """Тест проверяет вызов ошибки URLOrDataOnlyError"""

    with pytest.raises(URLOrDataOnlyError, match="Provide only one of url or data"):
        Scheduler(url="https", data={"data": [dict()]})
