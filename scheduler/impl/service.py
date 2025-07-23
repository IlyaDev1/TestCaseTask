from .mappers import str_to_date, time_to_str


def get_busy_slots(
    validated_days: list[dict], validated_timeslots: list[dict], date_value: str
) -> list[tuple[str, str]]:
    target_date = str_to_date(date_value)

    day = next((d for d in validated_days if d["date"] == target_date), None)
    if day is None:
        return []

    day_id = day["id"]
    return [
        (time_to_str(ts["start"]), time_to_str(ts["end"]))
        for ts in validated_timeslots
        if ts["day_id"] == day_id
    ]
