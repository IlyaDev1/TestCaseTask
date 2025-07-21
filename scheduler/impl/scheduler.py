from ..scheduler_interface import SchedulerInterface
from .schedule_loader import load_schedule


class Scheduler(SchedulerInterface):
    def __init__(
        self, url: str | None = None, data: dict[str, list[dict]] | None = None
    ) -> None:
        self.schedule: dict[str, list] = load_schedule(url, data)

    def get_busy_slots(self, date: str) -> list[tuple[str, str]]: ...  # type: ignore

    def get_free_slots(self, date: str) -> list[tuple[str, str]]: ...  # type: ignore

    def is_available(self, date: str, start_time: str, end_time: str) -> bool: ...  # type: ignore

    def find_slot_for_duration(  # type: ignore
        self, duration_minutes: int = 10
    ) -> tuple[str, str, str]: ...  # type: ignore
