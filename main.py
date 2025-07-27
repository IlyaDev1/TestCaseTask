import asyncio

from scheduler import Scheduler


async def main():
    scheduler = Scheduler()

    await scheduler.load_schedule_by_url(url="https://ofc-test-01.tspb.su/test-task/")

    # Получение всех занятых промежутков для даты 2025-02-15
    print(scheduler.get_busy_slots("2025-02-15"))

    # Получение всех свободных промежутков для даты 2025-02-15
    print(scheduler.get_free_slots("2025-02-15"))

    # Проверка доступности временного промежутка
    print(scheduler.is_available("2025-02-15", "12:00", "13:00"))

    print(scheduler.is_available("2025-02-15", "11:30", "12:30"))

    # Поиск первого подходящего свободного времени для заявки на 60 минут и на 90 минут
    print(scheduler.find_slot_for_duration(duration_minutes=60))

    print(scheduler.find_slot_for_duration(duration_minutes=90))


if __name__ == "__main__":
    asyncio.run(main())
