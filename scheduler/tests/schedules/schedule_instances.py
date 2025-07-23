from datetime import date, time

correct_schedule_by_url = {
    "days": [
        {
            "id": 1,
            "date": date(2025, 2, 15),
            "start": time(9, 0),
            "end": time(21, 0),
        },
        {
            "id": 2,
            "date": date(2025, 2, 16),
            "start": time(8, 0),
            "end": time(22, 0),
        },
        {
            "id": 3,
            "date": date(2025, 2, 17),
            "start": time(9, 0),
            "end": time(18, 0),
        },
        {
            "id": 4,
            "date": date(2025, 2, 18),
            "start": time(10, 0),
            "end": time(18, 0),
        },
        {
            "id": 5,
            "date": date(2025, 2, 19),
            "start": time(9, 0),
            "end": time(18, 0),
        },
    ],
    "timeslots": [
        {
            "id": 2,
            "day_id": 1,
            "start": time(9, 0),
            "end": time(12, 0),
        },
        {
            "id": 1,
            "day_id": 1,
            "start": time(17, 30),
            "end": time(20, 0),
        },
        {
            "id": 4,
            "day_id": 2,
            "start": time(9, 30),
            "end": time(11, 0),
        },
        {
            "id": 3,
            "day_id": 2,
            "start": time(14, 30),
            "end": time(18, 0),
        },
        {
            "id": 5,
            "day_id": 3,
            "start": time(12, 30),
            "end": time(18, 0),
        },
        {
            "id": 6,
            "day_id": 4,
            "start": time(10, 0),
            "end": time(11, 0),
        },
        {
            "id": 7,
            "day_id": 4,
            "start": time(11, 30),
            "end": time(14, 0),
        },
        {
            "id": 8,
            "day_id": 4,
            "start": time(14, 0),
            "end": time(16, 0),
        },
        {
            "id": 9,
            "day_id": 4,
            "start": time(17, 0),
            "end": time(18, 0),
        },
    ],
}


correct_schedule_by_dict = {
    "days": [
        {"id": 1, "date": date(2024, 10, 10), "start": time(9, 0), "end": time(18, 0)},
        {"id": 2, "date": date(2024, 10, 11), "start": time(8, 0), "end": time(17, 0)},
    ],
    "timeslots": [
        {"id": 1, "day_id": 1, "start": time(11, 0), "end": time(12, 0)},
        {"id": 3, "day_id": 2, "start": time(9, 30), "end": time(16, 0)},
    ],
}
