from datetime import date, datetime, time

from .exceptions import DayStructureError, TimeSlotStructureError


class ScheduleValidator:
    """Класс для валидации структуры данных расписания."""

    @staticmethod
    def is_keys_correct(data: dict) -> bool:
        """Проверяет, что словарь содержит ключи 'days' и 'timeslots'."""
        return tuple(data.keys()) == ("days", "timeslots")

    @staticmethod
    def is_days_timeslots_list(days, timeslots) -> bool:
        """Проверяет, что days и timeslots являются списками."""
        return isinstance(days, list) and isinstance(timeslots, list)

    @staticmethod
    def days_validator(days):
        """Проверяет и преобразует данные дней.

        Args:
            days: Список словарей с данными дней.

        Returns:
            Список дней с преобразованными датами и временем.

        Raises:
            DayStructureError: Если структура или формат данных некорректны.
        """
        validated_days = []
        for day in days:
            if not isinstance(day, dict):
                raise DayStructureError("Day must be a dictionary")
            if tuple(day.keys()) != ("id", "date", "start", "end"):
                raise DayStructureError(
                    f"Day {day} must have keys (id, date, start, end)"
                )

            id_value = day.get("id")
            if not isinstance(id_value, int):
                raise DayStructureError("Day id must be an integer")

            date_value = day.get("date")
            try:
                parsed_date = datetime.strptime(date_value, "%Y-%m-%d").date()
            except ValueError:
                raise DayStructureError(f"In {day}, date must be in YYYY-MM-DD format")

            start_value = day.get("start")
            end_value = day.get("end")
            try:
                start_time = datetime.strptime(start_value, "%H:%M").time()
                end_time = datetime.strptime(end_value, "%H:%M").time()
                if start_time >= end_time:
                    raise DayStructureError(
                        f"In {day}, start time must be before end time"
                    )
            except ValueError:
                raise DayStructureError(
                    f"In {day}, start and end must be in HH:MM format"
                )

            validated_days.append(
                {
                    "id": id_value,
                    "date": parsed_date,
                    "start": start_time,
                    "end": end_time,
                }
            )

        return validated_days

    @staticmethod
    def timeslots_validator(timeslots, day_ids):
        """Проверяет и преобразует данные таймслотов.

        Args:
            timeslots: Список словарей с данными таймслотов.
            day_ids: Множество ID дней для проверки day_id.

        Returns:
            Список таймслотов с преобразованными временем.

        Raises:
            TimeSlotStructureError: Если структура или формат данных некорректны.
        """
        validated_timeslots = []
        for timeslot in timeslots:
            if not isinstance(timeslot, dict):
                raise TimeSlotStructureError("Timeslot must be a dictionary")
            if tuple(timeslot.keys()) != ("id", "day_id", "start", "end"):
                raise TimeSlotStructureError(
                    f"Timeslot {timeslot} must have keys (id, day_id, start, end)"
                )

            id_value = timeslot.get("id")
            if not isinstance(id_value, int):
                raise TimeSlotStructureError("Timeslot id must be an integer")

            day_id_value = timeslot.get("day_id")
            if not isinstance(day_id_value, int):
                raise TimeSlotStructureError("Timeslot day_id must be an integer")
            if day_id_value not in day_ids:
                raise TimeSlotStructureError(
                    f"Timeslot day_id {day_id_value} does not match any day id"
                )

            start_value = timeslot.get("start")
            end_value = timeslot.get("end")
            try:
                start_time = datetime.strptime(start_value, "%H:%M").time()
                end_time = datetime.strptime(end_value, "%H:%M").time()
                if start_time >= end_time:
                    raise TimeSlotStructureError(
                        f"In {timeslot}, start time must be before end time"
                    )
            except ValueError:
                raise TimeSlotStructureError(
                    f"In {timeslot}, start and end must be in HH:MM format"
                )

            validated_timeslots.append(
                {
                    "id": id_value,
                    "day_id": day_id_value,
                    "start": start_time,
                    "end": end_time,
                }
            )

        return validated_timeslots
