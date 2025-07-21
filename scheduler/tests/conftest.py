import pytest

from scheduler import Scheduler


@pytest.fixture(scope="session", autouse=True)
def schedule_instance():
    yield Scheduler(url="https://ofc-test-01.tspb.su/test-task/")
