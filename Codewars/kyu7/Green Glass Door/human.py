def step_through_with(s):
    for i in s:
        if i + i in s:
            return True
    return False
