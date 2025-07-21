from datetime import date, time

correct_schedule_by_url = {
    "days": [
        {
            "id": 1,
            "date": date(2025, 2, 15),  # 15 февраля 2025 года
            "start": time(9, 0),  # 09:00
            "end": time(21, 0),  # 21:00
        },
        {
            "id": 2,
            "date": date(2025, 2, 16),  # 16 февраля 2025 года
            "start": time(8, 0),  # 08:00
            "end": time(22, 0),  # 22:00
        },
        {
            "id": 3,
            "date": date(2025, 2, 17),  # 17 февраля 2025 года
            "start": time(9, 0),  # 09:00
            "end": time(18, 0),  # 18:00
        },
        {
            "id": 4,
            "date": date(2025, 2, 18),  # 18 февраля 2025 года
            "start": time(10, 0),  # 10:00
            "end": time(18, 0),  # 18:00
        },
        {
            "id": 5,
            "date": date(2025, 2, 19),  # 19 февраля 2025 года
            "start": time(9, 0),  # 09:00
            "end": time(18, 0),  # 18:00
        },
    ],
    "timeslots": [
        {
            "id": 1,
            "day_id": 1,
            "start": time(17, 30),  # 17:30
            "end": time(20, 0),  # 20:00
        },
        {
            "id": 2,
            "day_id": 1,
            "start": time(9, 0),  # 09:00
            "end": time(12, 0),  # 12:00
        },
        {
            "id": 3,
            "day_id": 2,
            "start": time(14, 30),  # 14:30
            "end": time(18, 0),  # 18:00
        },
        {
            "id": 4,
            "day_id": 2,
            "start": time(9, 30),  # 09:30
            "end": time(11, 0),  # 11:00
        },
        {
            "id": 5,
            "day_id": 3,
            "start": time(12, 30),  # 12:30
            "end": time(18, 0),  # 18:00
        },
        {
            "id": 6,
            "day_id": 4,
            "start": time(10, 0),  # 10:00
            "end": time(11, 0),  # 11:00
        },
        {
            "id": 7,
            "day_id": 4,
            "start": time(11, 30),  # 11:30
            "end": time(14, 0),  # 14:00
        },
        {
            "id": 8,
            "day_id": 4,
            "start": time(14, 0),  # 14:00
            "end": time(16, 0),  # 16:00
        },
        {
            "id": 9,
            "day_id": 4,
            "start": time(17, 0),  # 17:00
            "end": time(18, 0),  # 18:00
        },
    ],
}
