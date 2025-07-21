from abc import ABC, abstractmethod


class SchedulerInterface(ABC):
    """Класс для работы с расписанием и заявками сотрудника.

    Предоставляет методы для получения занятых и свободных временных интервалов,
    проверки доступности времени и поиска подходящего слота для заявки заданной длительности.
    Использует данные, полученные через API по указанному URL или через словарь.

    Args:
        url (str | None): URL API для получения данных о расписании (например, "https://ofc-test-01.tspb.su/test-task/").
        data (dict[str, list[dict]] | None): Данные о расписании в формате {"days": [...], "timeslots": [...]}.
    """

    @abstractmethod
    def __init__(self, url: str | None, data: dict[str, list[dict]] | None) -> None:
        """Инициализирует класс данными расписания.

        Данные загружаются либо через API по указанному URL, либо из переданного словаря.
        Если переданы оба аргумента, приоритет отдается данным из словаря.
        """
        ...

    @abstractmethod
    def get_busy_slots(self, date: str) -> list[tuple[str, str]]:
        """Возвращает занятые промежутки времени сотрудника для указанной даты.

        Args:
            date (str): Дата в формате "гггг-мм-дд".

        Returns:
            list[tuple[str, str]]: Список кортежей с началом и концом занятых интервалов в формате "ЧЧ:ММ".
        """
        ...

    @abstractmethod
    def get_free_slots(self, date: str) -> list[tuple[str, str]]:
        """Возвращает свободные промежутки времени сотрудника для указанной даты.

        Args:
            date (str): Дата в формате "гггг-мм-дд".

        Returns:
            list[tuple[str, str]]: Список кортежей с началом и концом свободных интервалов в формате "ЧЧ:ММ".
        """
        ...

    @abstractmethod
    def is_available(self, date: str, start_time: str, end_time: str) -> bool:
        """Проверяет, свободен ли сотрудник в указанный день и временной промежуток.

        Args:
            date (str): Дата в формате "гггг-мм-дд".
            start_time (str): Начало интервала в формате "ЧЧ:ММ".
            end_time (str): Конец интервала в формате "ЧЧ:ММ".

        Returns:
            bool: True, если интервал свободен, иначе False.
        """
        ...

    @abstractmethod
    def find_slot_for_duration(self, duration_minutes: int = 10) -> tuple[str, str, str]:
        """Находит первое свободное время для заявки указанной длительности.

        Args:
            duration_minutes (int, optional): Продолжительность заявки в минутах. По умолчанию 10.

        Returns:
            tuple[str, str, str]: Кортеж (дата, начало, конец) в формате ("гггг-мм-дд", "ЧЧ:ММ", "ЧЧ:ММ").
        """
        ...
