from ..scheduler_interface import SchedulerInterface
from .schedule_loader import load_schedule
from .service import get_busy_slots as service_get_busy_slots


class Scheduler(SchedulerInterface):
    def __init__(
        self, url: str | None = None, data: dict[str, list[dict]] | None = None
    ) -> None:
        self.schedule: dict[str, list] = load_schedule(url, data)
        self.validated_days = self.schedule["days"]
        self.validated_timeslots = self.schedule["timeslots"]

    def get_busy_slots(self, date_value: str) -> list[tuple[str, str]]:
        return service_get_busy_slots(
            self.validated_days, self.validated_timeslots, date_value
        )

    def get_free_slots(self, date: str) -> list[tuple[str, str]]: ...  # type: ignore

    def is_available(self, date: str, start_time: str, end_time: str) -> bool: ...  # type: ignore

    def find_slot_for_duration(  # type: ignore
        self, duration_minutes: int = 10
    ) -> tuple[str, str, str]: ...  # type: ignore
