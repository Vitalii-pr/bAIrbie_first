def latest_clock(a, b, c, d):
    digits = [a, b, c, d]
    permutations = []
    for i in range(4):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    if i != j and i != k and i != l and j != k and j != l and k != l:
                        permutations.append([digits[i], digits[j], digits[k], digits[l]])

    valid_times = []
    for perm in permutations:
        hour_str = str(perm[0]) + str(perm[1])
        minute_str = str(perm[2]) + str(perm[3])

        # 24-hour validation (minutes now include 00)
        if (0 <= int(hour_str) <= 23) and (0 <= int(minute_str) <= 59): 
            valid_times.append(hour_str + ":" + minute_str)

    return max(valid_times) if valid_times else None
