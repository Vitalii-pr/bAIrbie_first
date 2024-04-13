def to_12_hour_time(time_string):
    hours = int(time_string[:2])  # Extract the hours part
    minutes = int(time_string[2:])  # Extract the minutes part

    if hours == 0:  # Special case for midnight
        return f"12:{minutes:02d} am"
    elif hours < 12:  # Morning (01:00 - 11:59)
        return f"{hours}:{minutes:02d} am"
    elif hours == 12:  # Noon
        return f"{hours}:{minutes:02d} pm"
    else:  # Afternoon/Evening (13:00 - 23:59) 
        return f"{hours - 12}:{minutes:02d} pm"
