correct_dirty_schedule = {  # Объект не обработанного расписания
    "days": [
        {"id": 1, "date": "2024-10-10", "start": "09:00", "end": "18:00"},
        {"id": 2, "date": "2024-10-11", "start": "08:00", "end": "17:00"},
    ],
    "timeslots": [
        {"id": 1, "day_id": 1, "start": "11:00", "end": "12:00"},
        {"id": 3, "day_id": 2, "start": "09:30", "end": "16:00"},
    ],
}
