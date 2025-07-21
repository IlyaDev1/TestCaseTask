class EmptyLoadDataError(ValueError):
    """Вызывается, если пользователь не передал ни URL, ни данные."""


class URLOrDataOnlyError(ValueError):
    """Вызывается, если пользователь передал одновременно URL и данные."""


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
