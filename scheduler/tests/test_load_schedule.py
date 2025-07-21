from scheduler import Scheduler


def test_correct_load_by_url(
    schedule_instance: Scheduler, correct_schedule_instance: dict
):
    assert schedule_instance.schedule == correct_schedule_instance
