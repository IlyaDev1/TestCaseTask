from abc import ABC, abstractmethod


class SchedulerInterface(ABC):
    """Класс для работы с расписанием и заявками сотрудника.

    Предоставляет методы для получения занятых и свободных временных интервалов,
    проверки доступности времени и поиска подходящего слота для заявки заданной длительности.
    Использует данные, полученные через API по указанному URL или через словарь.
    """

    @abstractmethod
    def __init__(self) -> None:
        """Определяет внутреннюю структуру хранения данных в классе."""
        pass

    @abstractmethod
    async def load_schedule_by_url(self, url: str) -> None:
        """Забирает данные о расписании по url и сохраняет в объект.

        Args:
            url: URL API для получения данных о расписании.
        """
        pass

    @abstractmethod
    def load_schedule_by_dict(self, data: dict) -> None:
        """Забирает данные о расписании через словарь в аргументе и сохраняет в объекте.

        Args:
            data: Слоаврь для получения данных о расписании.
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
    ) -> tuple[str, str, str] | None:
        """Находит первое свободное время для заявки указанной длительности.

        Args:
            duration_minutes: Продолжительность заявки в минутах. По умолчанию 10.

        Returns:
            Кортеж (дата, начало, конец) в формате ("гггг-мм-дд", "ЧЧ:ММ", "ЧЧ:ММ").
        """
        pass
