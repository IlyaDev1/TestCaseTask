class LoadByURLError(ValueError):
    """Вызывается при ошибке загрузки данных по URL."""


class ScheduleKeysError(ValueError):
    """Вызывается, если ключи словаря расписания некорректны."""


class ScheduleValuesError(ValueError):
    """Вызывается, если days или timeslots не являются списками."""


class DayStructureError(ValueError):
    """Вызывается, если структура данных дня некорректна."""


class TimeSlotStructureError(ValueError):
    """Вызывается, если структура данных таймслота некорректна."""


class DateDuplicateError(ValueError):
    """Вызывается, если есть дублирование даты в расписании."""


class SlotsIntersectionError(ValueError):
    """Вызывется, если есть пересечения в слотах времени на один день."""
