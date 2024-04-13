from datetime import datetime, timedelta
import bisect

def get_start_time(schedules, meeting_duration):
    busy_intervals = []
    for person_schedule in schedules:
        for start_str, end_str in person_schedule:
            start = datetime.strptime(start_str, "%H:%M")
            end = datetime.strptime(end_str, "%H:%M")
            while start < end:
                busy_intervals.append(start)
                start += timedelta(minutes=1)  

    busy_intervals.sort()

    start = datetime.strptime("09:00", "%H:%M")
    end = datetime.strptime("19:00", "%H:%M")

    while start < end:
        # Use binary search for the next busy interval
        idx = bisect.bisect_left(busy_intervals, start)
        if idx < len(busy_intervals):
            next_busy_start = busy_intervals[idx]
        else:
            next_busy_start = end  # No more busy intervals

        free_slot_duration = (next_busy_start - start).total_seconds() // 60 
        if free_slot_duration >= meeting_duration:
            return start.strftime("%H:%M")  
    
        start = next_busy_start + timedelta(minutes=1)  # Jump to the next free slot

    return None  # No suitable time found
