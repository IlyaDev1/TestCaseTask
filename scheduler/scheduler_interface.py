from abc import ABC, abstractmethod


class SchedulerInterface(ABC):
    """Класс для работы с расписанием и заявками сотрудника.

    Предоставляет методы для получения занятых и свободных временных интервалов,
    проверки доступности времени и поиска подходящего слота для заявки заданной длительности.
    Использует данные, полученные через API по указанному URL или через словарь.
    """

    @abstractmethod
    def __init__(
        self,
        url: str | None = None,
        data: dict | None = None,
    ) -> None:
        """Инициализирует класс данными расписания.

        Args:
            url: URL API для получения данных о расписании.
            data: Данные о расписании в формате {"days": [...], "timeslots": [...]}.

        Raises:
            ValueError: Если не передан ни url, ни data.
        """
        pass

    @abstractmethod
    def get_busy_slots(self, date: str) -> list[tuple[str, str]]:
        """Возвращает занятые промежутки времени сотрудника для указанной даты.

        Args:
            date: Дата в формате "гггг-мм-дд".

        Returns:
            Список кортежей с началом и концом занятых интервалов в формате "ЧЧ:ММ".
        """
        pass

    @abstractmethod
    def get_free_slots(self, date: str) -> list[tuple[str, str]]:
        """Возвращает свободные промежутки времени сотрудника для указанной даты.

        Args:
            date: Дата в формате "гггг-мм-дд".

        Returns:
            Список кортежей с началом и концом свободных интервалов в формате "ЧЧ:ММ".
        """
        pass

    @abstractmethod
    def is_available(self, date: str, start_time: str, end_time: str) -> bool:
        """Проверяет, свободен ли сотрудник в указанный день и временной промежуток.

        Args:
            date: Дата в формате "гггг-мм-дд".
            start_time: Начало интервала в формате "ЧЧ:ММ".
            end_time: Конец интервала в формате "ЧЧ:ММ".

        Returns:
            True, если интервал свободен, иначе False.
        """
        pass

    @abstractmethod
    def find_slot_for_duration(
        self, duration_minutes: int = 10
    ) -> tuple[str, str, str]:
        """Находит первое свободное время для заявки указанной длительности.

        Args:
            duration_minutes: Продолжительность заявки в минутах. По умолчанию 10.

        Returns:
            Кортеж (дата, начало, конец) в формате ("гггг-мм-дд", "ЧЧ:ММ", "ЧЧ:ММ").
        """
        pass
