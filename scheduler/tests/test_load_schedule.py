from scheduler import Scheduler

from .schedule_instances import correct_schedule_by_url


def test_correct_load_by_url(schedule_instance: Scheduler):
    """Тест проверяет, что c url данные загружаются корректно."""

    assert schedule_instance.schedule == correct_schedule_by_url
