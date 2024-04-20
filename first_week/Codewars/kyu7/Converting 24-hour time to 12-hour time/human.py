def to_12_hour_time(time_string):
    part_1, part_2 = int(time_string[:2]), time_string[2:]
    if 12 <= part_1:
        return f'{part_1 - 12 if part_1 != 12 else part_1}:{part_2} pm'
    if part_1 < 12:
        return f'{part_1 if part_1 != 0 else 12}:{part_2} am'
