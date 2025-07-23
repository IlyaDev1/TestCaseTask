from ..scheduler_interface import SchedulerInterface
from .schedule_loader import load_schedule
from .service import find_slot_for_duration as service_find_slot_for_duration
from .service import get_busy_slots as service_get_busy_slots
from .service import get_free_slots as service_get_free_slots
from .service import is_available as service_is_available


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

    def get_free_slots(self, date_value: str) -> list[tuple[str, str]]:
        return service_get_free_slots(
            self.validated_days, self.validated_timeslots, date_value
        )

    def is_available(self, date_value: str, start_time: str, end_time: str) -> bool:
        return service_is_available(
            date_value,
            start_time,
            end_time,
            self.validated_days,
            self.validated_timeslots,
        )

    def find_slot_for_duration(
        self, duration_minutes: int = 10
    ) -> tuple[str, str, str] | None:
        return service_find_slot_for_duration(
            self.validated_days, self.validated_timeslots, duration_minutes
        )
